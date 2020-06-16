from django.dispatch import receiver
from django.db.models.signals import post_save

from Statistics.models import DayBuyer, DaySeller, MouthBuyer, MouthSeller
from Tran.models import Task, Transaction
from Tran import utils as task_utils


@receiver(post_save, sender=Task)
def task_post_save(sender, instance=None, created=False, **kwargs):
    if not created:
        return
    for i in range(instance.batch_total):
        taskbatch = task_utils.taskbatch_add_one(instance, i+1)
        taskbatch.save()
        for transaction in task_utils.transaction_add_list(taskbatch):
            transaction.save()
            task_utils.transaction_add_statistics(transaction)
        # Transaction.objects.bulk_create(transaction_list)
    instance.status = True
    instance.save()