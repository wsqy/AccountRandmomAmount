import logging
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import transaction as shiwu

from Tran.models import Task, Transaction
from Account.models import Account
from Tran import utils as task_utils
from Tran.excel import CreateExcel, FujianTranExcel, TranInfoExcel, JiangxiTranExcel

logger = logging.getLogger('Tran')

@shiwu.atomic
@receiver(post_save, sender=Task)
def task_post_save(sender, instance=None, created=False, **kwargs):
    if not created:
        return

    # 事务--创建保存点
    save_id = shiwu.savepoint()

    # 初始化汇总表
    tran_huizong_excel = CreateExcel(instance)
    # 初始化转账信息表
    traninfo_excel = TranInfoExcel(instance)
    traninfo_count = 1
    logger.info('--准备为: %s 填充数据 ----' % instance)
    # 循环创建批次
    for i in range(instance.batch_total):
        logger.info('--准备生成第 %i 个交易批次----' % i)
        taskbatch = task_utils.taskbatch_add_one(instance, i+1)
        logger.info('--生成第 %i 个交易批次结束----'% i)
        if not taskbatch:
            logger.error('--第 %i 个交易批次生成不了 退出----'% i)

            # 事务 -- 回滚到保存点
            shiwu.savepoint_rollback(save_id)
            return 

        taskbatch.save()
        # 汇总表插入一条数据
        tran_huizong_excel.insert(taskbatch)

        # 初始化转账记录表
        if instance.corporation.template == '1':
            tran_excel = FujianTranExcel(taskbatch)
        else:
            tran_excel = JiangxiTranExcel(taskbatch)
        logger.info('--准备为第 %i 个批次添加交易记录----'% i)

        # 循环添加交易
        transaction_list = task_utils.transaction_add_list(taskbatch)
        logger.info('--为第 %i 个批次获取交易记录列表结束----'% i)
        if not transaction_list:
            # 异常退出
            logger.error('--为第 %i 个批次获取交易记录列表失败，推出----'% i)
            traninfo_excel.close()
            tran_huizong_excel.close()

            # 事务 -- 回滚到保存点
            shiwu.savepoint_rollback(save_id)

            return
        logger.info('--为第 %i 个批次获取交易记录列表成功， 准备写入数据----'% i)
        for j, transaction in enumerate(transaction_list, 2):
            # transaction.save()
            task_utils.transaction_add_statistics(transaction)
            # # 转账记录表&转账信息表插入一条数据
            account = Account.objects.filter(company=transaction.buyer.company).order_by('?').first()
            tran_excel.insert(j, transaction, account)
            traninfo_count += 1
            traninfo_excel.insert(traninfo_count, transaction)
        logger.info('--第 %i 个交易批次完成， 待写入表格, ----' % i)
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

    # 事务 -- 提交从保存点到当前状态的所有数据库事务操作
    shiwu.savepoint_commit(save_id)