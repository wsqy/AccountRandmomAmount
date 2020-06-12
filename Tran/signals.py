import time
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save

from Statistics.models import DayBuyer, DaySeller, MouthBuyer, MouthSeller
from Tran.models import Task, TaskBatch, Transaction
from Tran import utils as task_utils

@receiver(pre_save, sender=Task)
def task_pre_save(sender, instance=None, **kwargs):
    if not instance.name:
        instance.name = instance.show_date() + '任务'


@receiver(post_save, sender=Task)
def task_post_save(sender, instance=None, created=False, **kwargs):
    instance_list = TaskBatch.objects.filter(task=instance).values('num')
    if len(instance_list) != instance.batch_total:
        in_num_set = set([instance.get('num') for instance in instance_list])
        all_set = set(range(1, instance.batch_total+1))
        diff_set = all_set.difference(in_num_set)
        add_list = [task_utils.taskbatch_add_one(instance, i) for i in diff_set]
        TaskBatch.objects.bulk_create(add_list)


@receiver(post_save, sender=TaskBatch)
def taskbatch_post_save(sender, instance=None, created=False, **kwargs):
    instance_list = Transaction.objects.filter(task_batch=instance)
    diff_num = instance.batch_total - len(instance_list)
    if diff_num > 0:
        diff_amount = instance.amount_total - sum([instance.amount for instance in instance_list])
        print('1231111111')
        print(diff_amount)
        print('123111111')
        transaction_list = task_utils.transaction_add_list(instance, diff_amount, diff_num)
        Transaction.objects.bulk_create(transaction_list)
        # todo 添加卖方  买方数据，并测试该功能