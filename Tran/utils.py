import random
import string
from .models import Task, TaskBatch, Transaction
from Account.models import Buyer, Seller, Account
from Statistics.models import DayBuyer, DaySeller, MouthBuyer, MouthSeller, DayCompany, MouthCompany
from django.conf import settings 
from django.db.models import Q

def random_int(len=5):
    return ''.join(random.sample(string.digits, len))

def random_str(len=6):
    return ''.join(random.sample(string.ascii_letters + string.digits, len))

def get_download_zipfile(instance):
    date_str = instance.date.strftime('%Y-%m-%d')
    filepath = instance.date.strftime(r'/media/baobiao/%Y-%m/%d/')
    
    filename_content = '{}-{}'.format(date_str, instance.file_no)
    return filepath+filename_content+'.zip'

def get_download_excelfile(instance, type='转账文件'):
    date_str = instance.task.date.strftime('%Y-%m-%d')
    filepath = instance.task.date.strftime(r'/media/baobiao/%Y-%m/%d/')
    
    filename_content = '{}-{}'.format(date_str, instance.task.file_no)
    return '{}{}-{}-{}.xlsx'.format(filepath, filename_content, type, instance.num)

def taskbatch_add_one(task, _num):
    return TaskBatch(task=task, num=_num,
        batch_total=random.randint(task.batch_num_min, task.batch_num_max),
        amount_total=random.randint(task.amount_total_min, task.amount_total_max)
    )

def hongbao(_min=settings.DEFAULT_TRAN_MIN_AMOUNT, _max=settings.DEFAULT_TRAN_MAX_AMOUNT, total=0, num=0):
    hongbao_list = []
    if num < 1:
        return hongbao_list
    if num == 1:
        hongbao_list.append(total)
        return hongbao_list
    i = 1
    totalMoney = total
    while(i < num):
        _max = min(totalMoney - _min*(num-i), _max)
        monney = random.randint(_min, _max)
        totalMoney = totalMoney - monney
        hongbao_list.append(monney)
        i += 1
    hongbao_list.append(totalMoney)
    return hongbao_list


def transaction_add_list(instance):
    amount = instance.amount_total
    num = instance.batch_total
    while True:
        hongbao_list = hongbao(total=amount, num=num)
        if max(hongbao_list) < settings.DEFAULT_TRAN_MAX_AMOUNT:
            break
    transaction_list = []
    _date = instance.task.date
    for i in range(num):
        buyer = get_buyer(_date)
        seller = get_seller(buyer, _date)
        if (not buyer) or (not seller):
            return
        transaction_list.append(Transaction(task=instance.task, date=_date,
                                buyer=buyer, seller=seller,
                                amount=hongbao_list[i], task_batch=instance))
    return transaction_list

def transaction_add_statistics(transaction):
    daybuyer = DayBuyer.objects.select_for_update().get_or_create(buyer=transaction.buyer, date=transaction.date)[0]
    daybuyer.amount_total += transaction.amount
    daybuyer.save()

    dayseller = DaySeller.objects.select_for_update().get_or_create(seller=transaction.seller, date=transaction.date)[0]
    dayseller.amount_total += transaction.amount
    dayseller.save()

    daycompany = DayCompany.objects.select_for_update().get_or_create(company=transaction.buyer.company, date=transaction.date)[0]
    daycompany.amount_total += transaction.amount
    daycompany.save()

    mouthbuyer = MouthBuyer.objects.select_for_update().get_or_create(buyer=transaction.buyer, date=transaction.date.strftime("%Y年%m月"))[0]
    mouthbuyer.amount_total += transaction.amount
    mouthbuyer.save()

    mouthseller = MouthSeller.objects.select_for_update().get_or_create(seller=transaction.seller, date=transaction.date.strftime("%Y年%m月"))[0]
    mouthseller.amount_total += transaction.amount
    mouthseller.save()
    
    mouthcompany = MouthCompany.objects.select_for_update().get_or_create(company=transaction.buyer.company, date=transaction.date.strftime("%Y年%m月"))[0]
    mouthcompany.amount_total += transaction.amount
    mouthcompany.save()

def check_buy_mouth(buyer, date):
    """
    """
    # 否则月限额不是0:
        # 本月已交易金额是否超出？重试:return buyer
    # 如果月限额是0, 直接返回
    if buyer.mouth_total_max_limit == 0:
        return buyer
    # 否则 月限额不是0
    else:
        try:
            # 先看看有没有记录，有记录就判断是否超了
            mouth_total = MouthBuyer.objects.get(buyer=buyer, date=date.strftime("%Y年%m月"))
            # 本月已交易金额是否超出？重试:return buyer
            if mouth_total.amount_total > buyer.mouth_total_max_limit:
                return None
            else:
                return buyer
        except Exception as e:
            # 找不到数据说明本月还没有交易, 那肯定没超
            return buyer

def get_buyer(date):
    buy_list = Buyer.objects.filter(is_activate=True)
    if buy_list.count() == 0:
        return 
    nums = 0
    while True:
        if nums > 10:
            return 
        nums += 1
        buyer = random.choice(buy_list)
        if buyer.day_total_max_limit == 0:
            if check_buy_mouth(buyer, date):
                return buyer
            else:
                continue
        else:
            # 否则 日限额不是0
            try:
                day_total = DayBuyer.objects.get(buyer=buyer, date=date)
                if day_total.amount_total > buyer.day_total_max_limit:
                    continue
                else:
                    # 月限额测试
                    if check_buy_mouth(buyer, date):
                        return buyer
                    else:
                        continue
            except Exception as e:
                return  buyer

def check_seller_mouth(seller, date):
    """
    """
    if seller.mouth_total_max_limit == 0:
        return seller
    else:
        try:
            # 先看看有没有记录，有记录就判断是否超了
            mouth_total = MouthSeller.objects.get(seller=seller, date=date.strftime("%Y年%m月"))
            # 本月已交易金额是否超出？重试:return buyer
            if mouth_total.amount_total > seller.mouth_total_max_limit:
                return None
            else:
                return seller
        except Exception as e:
            # 找不到数据说明本月还没有交易, 那肯定没超
            return seller

def get_seller(buyer, date):
    seller_list = Seller.objects.filter(is_activate=True, scope=buyer.scope)
    if seller_list.count() == 0:
        return 
    nums = 0
    while True:
        if nums > 10:
            return 
        nums += 1
        seller = random.choice(seller_list)
        if seller.day_total_max_limit == 0:
            if check_seller_mouth(seller, date):
                return seller
            else:
                continue
        else:
            # 否则 日限额不是0
            try:
                day_total = DaySeller.objects.get(seller=seller, date=date)
                if day_total.amount_total > seller.day_total_max_limit:
                    continue
                else:
                    # 月限额测试
                    if check_seller_mouth(seller, date):
                        return seller
                    else:
                        continue
            except Exception as e:
                return  seller
