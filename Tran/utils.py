import random
import string
from .models import Task, TaskBatch, Transaction
from Account.models import Buyer, Seller, Account, Products, Company
from Statistics.models import (DayBuyer, DaySeller, MouthBuyer, MouthSeller,
                                DayCompany, MouthCompany, DaySellerProducts)
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
    corporation = task.corporation

    nums = 0
    while True:
        if nums > 50:
            return 
        nums += 1
        batch_total=random.randint(task.batch_num_min, task.batch_num_max)
        limit_min = batch_total * settings.DEFAULT_TRAN_MIN_AMOUNT
        limit_max = batch_total * settings.DEFAULT_TRAN_MAX_AMOUNT
        amount_total=random.randint(max(task.amount_total_min, limit_min), min(task.amount_total_max, limit_max))
        print("OAAAAOOOO\n" * 2)
        print(batch_total, amount_total)
        if (limit_min < amount_total) and ( limit_max> amount_total):
            return TaskBatch(task=task, num=_num, batch_total=batch_total, amount_total=amount_total)

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

def get_total_range(amount):
    if amount > 500:
        return 3
    elif amount < 200:
        return 1
    return 2

def get_products(total_range, scope):
    return Products.objects.filter(is_activate=True, total_range__contains=total_range, scope=scope).order_by('?').first()

def transaction_add_list(instance):
    amount = instance.amount_total
    corporation = instance.task.corporation
    num = instance.batch_total
    company_list = get_company_list(corporation, num)
    print('-company_list--')
    print(company_list)
    nums = 0
    while True:
        if nums > 10:
            return 
        nums += 1
        hongbao_list = hongbao(total=amount, num=num)
        print('-hongbao_list--')
        print(hongbao_list)
        if (max(hongbao_list) < settings.DEFAULT_TRAN_MAX_AMOUNT) and (min(hongbao_list) > settings.DEFAULT_TRAN_MIN_AMOUNT):
            break
    transaction_list = []
    _date = instance.task.date
    for i, company in enumerate(company_list, 0):
        amount = hongbao_list[i]
        total_range = get_total_range(amount)
        max_try = 0
        while True:
            max_try += 1
            if max_try > 100:
                return[]
            buyer = get_buyer(total_range, _date, company)
            print('---buyer---')
            print(buyer)
            if not buyer:
                continue
            scope = buyer.scope
            products = get_products(total_range, scope)
            print('--products---')
            print(products)
            if not products:
                continue

            seller = get_seller(scope)
            print('--seller---')
            print(seller)
            if not seller:
                continue
            price = get_price(seller, products)
            quantity = int(amount*10000/0.3/price)
            for i in range(10):
                real_amount = round(quantity * price *0.3 / 10000, 0)
                if real_amount ==  amount:
                    break
                elif real_amount <  amount:
                    quantity += 1
                elif real_amount >  amount:
                    quantity -= 0.5
                    break

            transaction = Transaction(task=instance.task, date=_date,
                                        buyer=buyer, seller=seller,
                                        amount=amount, task_batch=instance,
                                        price=price, products=products,
                                        total_range=total_range, quantity=quantity,
                                        tran_tatal=int(price*quantity),
                                        order_no='{0}{1:%Y%m%d}{2:0>3}{3:0>3}{4:0>3}'.format(buyer.company.company_code, instance.task.date, random_int(3), str(instance.num)[-3:], str(i+1)[-3:])
            )
            transaction.save()    
            transaction_list.append(transaction)
            print('添加完成一条记录%s' % instance.num)
            break
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

    daysellerproducts = DaySellerProducts.objects.select_for_update().get_or_create(seller=transaction.seller, date=transaction.date, products=transaction.products)[0]
    daysellerproducts.price = transaction.price
    daysellerproducts.quantity += (int(transaction.quantity) * int(daysellerproducts.choice_scale))
    daysellerproducts.save()

def get_price(seller, products):
    try:
        transaction = Transaction.objects.get(seller=seller, products=products)
        return transaction.price
    except Exception as e:
        return random.randint(products.price_min, products.price_max)


def get_buyer(total_range, date, company):
    _year = date.year
    _month = date.month
    for i in range(settings.SEARCH_BUSINESSCOMPANY_LIMIT):
        buyer_list = Buyer.objects.filter(is_activate=True, total_range=total_range, company=company).order_by('?')[:settings.SEARCH_BUSINESSCOMPANY_PER_LIMIT]
        for buyer in buyer_list:
            mouth_total = Transaction.objects.filter(buyer=buyer, total_range=total_range, date__month=_month, date__year=_year).count()
            if mouth_total < buyer.mouth_buy_limit:
                return buyer


def get_seller(scope):
    return Seller.objects.filter(is_activate=True, scope=scope).order_by('?').first()

def get_company_list(corporation, num):
    def countX(company_list, company):
        if len(company_list) < 2:
            return 0
        count = 0
        for ele in company_list:
            if (ele.id == company.id):
                count = count + 1
        return count

    print("集团: %s, 总笔数: %s" % (corporation.name, num))
    company_list = Company.objects.filter(is_activate=True, corporation=corporation).order_by('?')
    print(company_list)
    max_in = max((num//company_list.count()) * 2, 1)
    print('子公司最多出现: %s 次' % max_in)
    new_company_list = []
    for i in range(1000):
        if len(new_company_list) == num:
            return new_company_list
        company = random.choice(company_list)
        print('---子公司 start----')
        print(company)
        print('---子公司 end----')
        if countX(new_company_list, company) < max_in:
            new_company_list.append(company)
        print('---子公司列表 start----')
        print(new_company_list)
        print('---子公司列表 end----')
    return company_list

def get_company_count(corporation):
    return Company.objects.filter(is_activate=True, corporation=corporation).count()
