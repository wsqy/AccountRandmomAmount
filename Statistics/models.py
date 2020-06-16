from django.db import models
# from django.conf import settings
from django.utils import timezone
from Account.models import Buyer, Seller

class DayBuyer(models.Model):
    """
    日买方交易额总量表
    """
    date = models.DateField(verbose_name='任务日期', default=timezone.now)
    buyer = models.ForeignKey(Buyer, on_delete=models.PROTECT, verbose_name='买方')
    amount_total = models.IntegerField(verbose_name='日总交易金额(万元)', default=0)

    class Meta:
        verbose_name = '日买方交易额总量'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}于{}总交易额{}万元'.format(self.buyer, self.date, self.amount_total)


class DaySeller(models.Model):
    """
    日卖方交易额总量表
    """
    date = models.DateField(verbose_name='任务日期', default=timezone.now)
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT, verbose_name='卖方')
    amount_total = models.IntegerField(verbose_name='日总交易金额(万元)', default=0)

    class Meta:
        verbose_name = '日卖方交易额总量'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}于{}总交易额{}万元'.format(self.seller, self.date, self.amount_total)


class MouthBuyer(models.Model):
    """
    月买方交易额总量表
    """
    date = models.CharField(max_length=6, verbose_name='月份', blank=True, null=True,)
    buyer = models.ForeignKey(Buyer, on_delete=models.PROTECT, verbose_name='买方')
    amount_total = models.IntegerField(verbose_name='月总交易金额(万元)', default=0)

    class Meta:
        verbose_name = '月买方交易额总量'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}于{}总交易额{}万元'.format(self.buyer, self.mouth, self.amount_total)


class MouthSeller(models.Model):
    """
    月卖方交易额总量表
    """
    date = models.CharField(max_length=6, verbose_name='月份', blank=True, null=True,)
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT, verbose_name='卖方')
    amount_total = models.IntegerField(verbose_name='月总交易金额(万元)', default=0)

    class Meta:
        verbose_name = '月卖方交易额总量'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}于{}总交易额{}万元'.format(self.seller, self.mouth, self.amount_total)