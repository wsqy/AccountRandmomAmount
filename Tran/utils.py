import random

from Tran.models import TaskBatch, Transaction
from Account.models import Buyer, Seller

def taskbatch_add_one(task, _num):
    return TaskBatch(task=task, num=_num, remark=task.remark,
        batch_total=random.randint(task.batch_num_min, task.batch_num_max),
        amount_total=random.randint(task.amount_total_min, task.amount_total_max)
    )

def hongbao(_min=50, _max=950, total=0, num=0):
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
        if max(hongbao_list) < 950:
            break
    # 随机获取num个买方
    buyer_list = Buyer.objects.all().order_by('?')[:num]
    # 根据买方公司分类获取随机匹配卖方
    seller_list = [Seller.objects.filter(scope=buyer.scope).order_by('?').first() for buyer in buyer_list]
    return [Transaction(task=instance.task, task_batch=instance, remark=instance.remark,
     buyer=buyer_list[i], seller=seller_list[i], amount=hongbao_list[i]) for i in range(num)]