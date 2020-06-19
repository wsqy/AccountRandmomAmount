from django.db import models
# from django.conf import settings
from django.utils import timezone
from Account.models import Buyer, Seller, Company

class DayBuyer(models.Model):
    """
    买方日交易额总量表
    """
    date = models.DateField(verbose_name='任务日期', default=timezone.now)
    buyer = models.ForeignKey(Buyer, on_delete=models.PROTECT, verbose_name='买方')
    amount_total = models.IntegerField(verbose_name='日总交易金额(万元)', default=0)

    class Meta:
        verbose_name = '买方日交易额总量'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}于{}总交易额{}万元'.format(self.buyer, self.date, self.amount_total)


class DaySeller(models.Model):
    """
    卖方日交易额总量表
    """
    date = models.DateField(verbose_name='任务日期', default=timezone.now)
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT, verbose_name='卖方')
    amount_total = models.IntegerField(verbose_name='日总交易金额(万元)', default=0)

    class Meta:
        verbose_name = '卖方日交易额总量'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}于{}总交易额{}万元'.format(self.seller, self.date, self.amount_total)


class DayCompany(models.Model):
    """
    集团子公司日交易额总量表
    """
    date = models.DateField(verbose_name='任务日期', default=timezone.now)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, verbose_name='卖方')
    amount_total = models.IntegerField(verbose_name='日总交易金额(万元)', default=0)

    class Meta:
        verbose_name = '集团子公司日交易额总量'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}于{}总交易额{}万元'.format(self.company, self.date, self.amount_total)


class MouthBuyer(models.Model):
    """
    买方月交易额总量表
    """
    date = models.CharField(max_length=8, verbose_name='月份')
    buyer = models.ForeignKey(Buyer, on_delete=models.PROTECT, verbose_name='买方')
    amount_total = models.IntegerField(verbose_name='月总交易金额(万元)', default=0)

    class Meta:
        verbose_name = '买方月交易额总量'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}于{}总交易额{}万元'.format(self.buyer, self.date, self.amount_total)


class MouthSeller(models.Model):
    """
    卖方月交易额总量表
    """
    date = models.CharField(max_length=8, verbose_name='月份')
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT, verbose_name='卖方')
    amount_total = models.IntegerField(verbose_name='月总交易金额(万元)', default=0)

    class Meta:
        verbose_name = '卖方月交易额总量'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}于{}总交易额{}万元'.format(self.seller, self.date, self.amount_total)
        

class MouthCompany(models.Model):
    """
    集团子公司月交易额总量表
    """
    date = models.CharField(max_length=8, verbose_name='月份')
    company = models.ForeignKey(Company, on_delete=models.PROTECT, verbose_name='卖方')
    amount_total = models.IntegerField(verbose_name='月总交易金额(万元)', default=0)

    class Meta:
        verbose_name = '集团子公司月交易额总量'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}于{}总交易额{}万元'.format(self.company, self.date, self.amount_total)