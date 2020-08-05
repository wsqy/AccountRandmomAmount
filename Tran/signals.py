from django.dispatch import receiver
from django.db.models.signals import post_save

from Tran.models import Task, Transaction
from Account.models import Account
from Tran import utils as task_utils
from Tran.excel import CreateExcel, FujianTranExcel, TranInfoExcel, JiangxiTranExcel


@receiver(post_save, sender=Task)
def task_post_save(sender, instance=None, created=False, **kwargs):
    if not created:
        return
    # 初始化汇总表
    tran_huizong_excel = CreateExcel(instance)
    # 循环创建批次
    for i in range(instance.batch_total):
        taskbatch = task_utils.taskbatch_add_one(instance, i+1)
        print('taskbatch--_9999999----\n' * 2)
        if not taskbatch:
            print('-交易批次生成不了 退出----\n' * 2)
            return 
        taskbatch.save()
        # 汇总表插入一条数据
        tran_huizong_excel.insert(taskbatch)

        # 初始化转账记录表
        if instance.corporation.template == '1':
            tran_excel = FujianTranExcel(taskbatch)
        else:
            tran_excel = JiangxiTranExcel(taskbatch)
        print('--_9999999----\n' * 2)
        # 初始化转账信息表
        traninfo_excel = TranInfoExcel(taskbatch)
        # print('--_FFFFFFFFFFFFFFFFFFFFF----\n' * 2)
        # 循环添加交易
        transaction_list = task_utils.transaction_add_list(taskbatch)
        # print('ZZZXXXXXXZZFFFFFFFFFFF----\n' * 2)
        if not transaction_list:
            # 异常退出
            print('-交易表生成不了 退出----\n' * 2)
            traninfo_excel.close()
            tran_huizong_excel.close()
            return
        # print('--MMMMMM---\n' * 2)
        for j, transaction in enumerate(transaction_list, 2):
            # transaction.save()
            task_utils.transaction_add_statistics(transaction)
            # # 转账记录表&转账信息表插入一条数据
            account = Account.objects.filter(company=transaction.buyer.company).order_by('?').first()
            tran_excel.insert(j, transaction, account)
            traninfo_excel.insert(j, transaction)
        print('-AAAAAAAAAAA----\n' * 2)
        # 写入转账记录表&转账信息表
        tran_excel.close()
        traninfo_excel.close()

    # 写入 汇总表
    tran_huizong_excel.close()
    # 创建zip文件
    tran_huizong_excel.creat_zipfile()
    # 设置任务已完成
    instance.status = True
    instance.save()