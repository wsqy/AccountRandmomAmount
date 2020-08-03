from django.db import models
# from django.conf import settings
from django.utils import timezone

# Create your models here.

class Company(models.Model):
    """
    子公司表
    """
    
    CORPORATION = (
        ('1', '默认集团'),
    )
    
    name = models.CharField(max_length=40, verbose_name='子公司名称',
                            blank=False, help_text='子公司名称')
    corporation = models.CharField(max_length=2, blank=False, null=False, choices=CORPORATION, default='1',
                                    verbose_name='所属集团', help_text='子公司所属集团, 默认1')
    is_activate = models.BooleanField(default=True, verbose_name='状态',)

    class Meta:
        verbose_name = '集团子公司'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BusinessScope(models.Model):
    """
    经营分类
    """
    name = models.CharField(max_length=40, verbose_name='经营分类', blank=False, null=False, help_text='经营分类')
    is_activate = models.BooleanField(default=True, verbose_name='状态',)

    class Meta:
        verbose_name = '经营分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Products(models.Model):
    """
    商品表
    """
    TOTAL = (
        ('1', '200万以内'),
        ('2', '200万-500万'),
        ('3', '超过500万'),
    )
    scope = models.ForeignKey(BusinessScope, on_delete=models.PROTECT, verbose_name='分类', blank=False, null=False, help_text='大的经营分类')
    name = models.CharField(max_length=40, verbose_name='商品名称', blank=False, null=False, help_text='商品名称')
    type = models.CharField(max_length=511, verbose_name='商品型号', blank=False, null=False, help_text='商品型号')
    price_min = models.PositiveIntegerField(verbose_name='单价下限', help_text='单价下限(包含)', blank=False, null=False)
    price_max = models.PositiveIntegerField(verbose_name='单价上限', help_text='单价上限(包含)', blank=False, null=False)
    unit = models.CharField(max_length=40, verbose_name='计量单位', blank=False, null=False, help_text='计量单位')
    total_range = models.CharField(choices=TOTAL, max_length=1, verbose_name='总价范围', blank=False, null=False, help_text='总价范围')
    is_activate = models.BooleanField(default=True, verbose_name='状态',)

    class Meta:
        verbose_name = '商品表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BusinessCompany(models.Model):
    """
    交易公司表
    """
    name = models.CharField(max_length=40, verbose_name='公司名称', blank=False, null=False, help_text='公司名称')
    scope = models.ForeignKey(BusinessScope, on_delete=models.PROTECT, verbose_name='公司经营分类', blank=False, null=False, )
    is_activate = models.BooleanField(default=True, verbose_name='状态', blank=False, null=False, )
    mouth_total_max_limit = models.PositiveIntegerField(verbose_name='月上限(万元)', help_text='设置为0代表不设置上限', blank=False, null=False, default=0)
    day_total_max_limit = models.PositiveIntegerField(verbose_name='日上限(万元)', help_text='设置为0代表不设置上限', blank=False, null=False, default=0)
    
    class Meta:
        verbose_name = '交易公司'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Buyer(BusinessCompany):
    """
    买方表
    """
    # single_min = models.PositiveIntegerField(verbose_name='单笔交易下限(万元)', help_text='设置为0代表不设置下限',
    #                                          default=50, blank=False, null=False, )
    # single_max = models.PositiveIntegerField(verbose_name='单笔交易上限(万元)', help_text='设置为0代表不设置上限',
    #                                          default=950, blank=False, null=False, )
    company = models.ForeignKey(Company, on_delete=models.PROTECT, verbose_name='所属子公司')
    
    class Meta:
        verbose_name = '买方'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Seller(BusinessCompany):
    """
    卖方表
    """

    class Meta:
        verbose_name = '卖方'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Account(models.Model):
    """
    账号表
    """
    company = models.ForeignKey(Company, on_delete=models.PROTECT, verbose_name='所属集团子公司')
    account_name = models.CharField(max_length=40, verbose_name='账号名称', blank=False, null=False, help_text='账号名称')
    account = models.CharField(max_length=40, verbose_name='账号', blank=False, null=False, help_text='账号')
    bank_name = models.CharField(max_length=40, verbose_name='开户行名称', blank=False, null=False, help_text='开户行名称')
    bank_code = models.CharField(max_length=40, verbose_name='开户行号', blank=False, null=False, help_text='开户行号')
    class Meta:
        verbose_name = '账号'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.account_name
