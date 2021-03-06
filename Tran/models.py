import time
import datetime
from django.db import models
from django.utils import timezone
from Account.models import Buyer, Seller, Account
# from .utils import random_str
import random
import string

def random_str(len=6):
    return ''.join(random.sample(string.ascii_letters + string.digits, len))

class Task(models.Model):
    """
    每日任务表
    """
    TEMPLATE = (
        ('1', '福建模板'),
        ('2', '江西模板'),
    )
    date = models.DateField(verbose_name='任务日期', blank=False,null=False,
                            default=timezone.now, )
    name = models.CharField(max_length=40, verbose_name='任务名称', blank=True, null=True,
                            help_text='同一日有多个任务最好设置本次任务名称')
    amount_total_min = models.PositiveIntegerField(verbose_name='每日总金额下限',
                                                   blank=False, null=False, )
    amount_total_max = models.PositiveIntegerField(verbose_name='每日总金额上限',
                                                   blank=False, null=False, )
    batch_total = models.PositiveSmallIntegerField(verbose_name='批次数', default=30,
                                                   blank=False, null=False,)
    batch_num_min = models.PositiveSmallIntegerField(verbose_name='每批次交易笔数下限',
                                                     blank=False, null=False, default=3)
    batch_num_max = models.PositiveSmallIntegerField(verbose_name='每批次交易笔数上限', 
                                                     blank=False, null=False, default=7)
    status = models.BooleanField(default=False, verbose_name='是否完成', blank=False, null=False)
    remark = models.CharField(max_length=40, verbose_name='交易备注', blank=True, null=True,
                              help_text='该备注信息会自动填充到每笔转账备注中')
    file_no = models.CharField(max_length=6, verbose_name='文件编号', blank=False,
                               null=False, default=random_str)
    template = models.CharField(max_length=2, verbose_name='文件模板', choices=TEMPLATE,
                                blank=False,null=False, default='1')
    
    class Meta:
        verbose_name = '每日任务'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.show_date()
    
    def show_date(self):
        return self.date.strftime('%Y-%m-%d')


class TaskBatch(models.Model):
    """
    任务批次表
    """
    task = models.ForeignKey(Task, on_delete=models.PROTECT, verbose_name='所属日任务')
    amount_total = models.PositiveIntegerField(verbose_name='批次总金额',
                                                blank=False, null=False, )
    batch_total = models.PositiveSmallIntegerField(verbose_name='批次交易笔数',
                                                    blank=False, null=False, default=3)
    num = models.PositiveSmallIntegerField(verbose_name='批次编号', blank=False, null=False)

    class Meta:
        verbose_name = '任务批次'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}-{}'.format(self.task, self.num)


class Transaction(models.Model):
    """
    交易明细表
    """
    task = models.ForeignKey(Task, on_delete=models.PROTECT, verbose_name='所属日任务')
    task_batch = models.ForeignKey(TaskBatch, on_delete=models.PROTECT, verbose_name='所属日批次')
    buyer = models.ForeignKey(Buyer, on_delete=models.PROTECT, verbose_name='买方')
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT, verbose_name='卖方')
    date = models.DateField(verbose_name='任务日期', blank=False,null=False, default=timezone.now)
    amount = models.IntegerField(verbose_name='交易金额', blank=False, null=False, )

    class Meta:
        verbose_name = '交易明细'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}向{}购买{}元'.format(self.buyer,self.seller, self.amount)
