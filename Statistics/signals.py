from django.dispatch import receiver
from django.db.models.signals import post_save

from Statistics.models import DayBuyer, DaySeller, MouthBuyer, MouthSeller

from Tran.models import Task, TaskBatch, Transaction


# @receiver(post_save, sender=Task)
# def balance_detail_create(sender, instance=None, created=False, **kwargs):
#     if created:
#         print('1111111111\n'*5)