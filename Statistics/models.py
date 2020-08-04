import random
from django.db import models
# from django.conf import settings
from django.utils import timezone
from Account.models import Buyer, Seller, Company, Products

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
    company = models.ForeignKey(Company, on_delete=models.PROTECT, verbose_name='集团子公司')
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
    company = models.ForeignKey(Company, on_delete=models.PROTECT, verbose_name='集团子公司')
    amount_total = models.IntegerField(verbose_name='月总交易金额(万元)', default=0)

    class Meta:
        verbose_name = '集团子公司月交易额总量'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}于{}总交易额{}万元'.format(self.company, self.date, self.amount_total)


class DaySellerProducts(models.Model):
    "卖方每日销售表"
        
    def random_choice_scale():
        return random.randint(2, 10)

    date = models.DateField(verbose_name='任务日期', default=timezone.now)
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT, verbose_name='卖方')
    products = models.ForeignKey(Products, on_delete=models.PROTECT, verbose_name='购买商品')
    price = models.PositiveIntegerField(verbose_name='购买单价', help_text='购买单价', blank=False, null=False)
    quantity = models.PositiveIntegerField(verbose_name='订货量', help_text='订货量', blank=False, null=False)
    choice_scale = models.PositiveIntegerField(verbose_name='备货比例', help_text='备货比例',
                                                blank=False, null=False, default=random_choice_scale)

    class Meta:
        verbose_name = '卖方每日销售表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}于{}卖了{}{}{}'.format(self.seller, self.date, self.quantity,
                                         self.products.unit, self.products.name)
