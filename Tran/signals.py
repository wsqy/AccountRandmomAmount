from django.dispatch import receiver
from django.db.models.signals import post_save

from Tran.models import Task, Transaction
from Account.models import Account
from Tran import utils as task_utils
from Tran.excel import FujianHuizongExcel, FujianTranExcel


@receiver(post_save, sender=Task)
def task_post_save(sender, instance=None, created=False, **kwargs):
    if not created:
        return
    # 初始化汇总表
    tran_huizong_excel = FujianHuizongExcel(instance)

    # 循环创建批次
    for i in range(instance.batch_total):
        taskbatch = task_utils.taskbatch_add_one(instance, i+1)
        taskbatch.save()
        # 汇总表插入一条数据
        tran_huizong_excel.insert(taskbatch)

        # 初始化交易表
        tran_excel = FujianTranExcel(taskbatch)

        # 循环添加交易
        for j, transaction in enumerate(task_utils.transaction_add_list(taskbatch), 2):
            transaction.save()
            task_utils.transaction_add_statistics(transaction)
            # 交易表插入一条数据
            account = Account.objects.filter(company=transaction.buyer.company).order_by('?').first()
            tran_excel.insert(j, transaction, account)
        # 写入交易表
        tran_excel.close() 

    # 写入 汇总表
    tran_huizong_excel.close()
    # 创建zip文件
    tran_huizong_excel.creat_zipfile()
    # 设置任务已完成
    instance.status = True
    instance.save()