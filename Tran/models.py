import time
import datetime
from django.db import models
from django.utils import timezone
from Account.models import Buyer, Seller


class Task(models.Model):
    """
    每日任务表
    """
    date = models.DateField(verbose_name='任务日期', blank=False,null=False,
                            default=timezone.now, )
    name = models.CharField(max_length=40, verbose_name='批次名称', blank=True, null=True,
                             help_text='同一日有多个批次任务最好设置批次名称')
    amount_total_min = models.PositiveIntegerField(verbose_name='每日总金额下限',
                                                    blank=False, null=False, )
    amount_total_max = models.PositiveIntegerField(verbose_name='每日总金额上限', 
                                                    blank=False, null=False, )
    batch_total = models.PositiveSmallIntegerField(verbose_name='批次数', default=30,
                                                    blank=False, null=False, )
    batch_num_min = models.PositiveSmallIntegerField(verbose_name='每批次交易笔数下限',
                                                     blank=False, null=False, default=3)
    batch_num_max = models.PositiveSmallIntegerField(verbose_name='每批次交易笔数上限', 
                                                     blank=False, null=False, default=7)
    status = models.BooleanField(default=False, verbose_name='是否完成', blank=False, null=False, )
    remark = models.CharField(max_length=40, verbose_name='交易备注', blank=True, null=True,)
    download_link = models.CharField(max_length=100, verbose_name='下载地址', blank=True, null=True,)
    
    class Meta:
        verbose_name = '每日任务'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.show_date()
            # return self.date
    
    def show_date(self):
        # _time = time.localtime(self.date)
        return self.date.strftime('%Y-%m-%d')

class TaskBatch(models.Model):
    """
    任务批次表
    """
    STATUS = (
        ('1', '批次未开始'),
        ('20', '批次明细生成中'),
        ('21', '批次明细生成完成'),
        ('99', '任务作废')
    )
    task = models.ForeignKey(Task, on_delete=models.PROTECT, verbose_name='所属日任务')
    amount_total = models.PositiveIntegerField(verbose_name='批次总金额',
                                                blank=False, null=False, )
    batch_total = models.PositiveSmallIntegerField(verbose_name='批次交易笔数',
                                                    blank=False, null=False, default=3)
    num = models.PositiveSmallIntegerField(verbose_name='批次编号', blank=False, null=False)
    remark = models.CharField(max_length=40, verbose_name='交易备注', blank=True, null=True,)

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
    task_batch = models.ForeignKey(TaskBatch, on_delete=models.PROTECT,
                                    verbose_name='所属日批次')
    buyer = models.ForeignKey(Buyer, on_delete=models.PROTECT, verbose_name='买方')
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT, verbose_name='卖方')
    date = models.DateField(verbose_name='任务日期', blank=False,null=False,
                            default=timezone.now, )
    amount = models.IntegerField(verbose_name='交易金额', blank=False, null=False, )
    remark = models.CharField(max_length=40, verbose_name='交易备注', blank=True, null=True,)

    class Meta:
        verbose_name = '交易明细'
        verbose_name_plural = verbose_name

    def __str__(self):
        return_str = '{}向{}购买{}元'.format(self.buyer,self.seller, self.amount)
        if self.remark:
            return_str = '{}, 备注{}'.format(self.remark)
        return return_str
