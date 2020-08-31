from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Corporation(models.Model):    
    """
    交易场所表
    """
    TEMPLATE = (
        ('1', '福建模板'),
        ('2', '江西模板'),
    )
    name = models.CharField(max_length=40, verbose_name='交易场所名称', blank=False, null=False, help_text='交易场所')
    template = models.CharField(max_length=2, verbose_name='转账文件模板', choices=TEMPLATE,
                                blank=False, null=False)
    is_activate = models.BooleanField(default=True, verbose_name='状态', blank=True, null=True, help_text='该交易场所是否继续使用')

    class Meta:
        verbose_name = '交易场所'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Company(models.Model):
    """
    集团子公司表
    """
    name = models.CharField(max_length=40, verbose_name='子公司名称', blank=False, help_text='子公司名称')
    corporation = models.ForeignKey(Corporation, on_delete=models.CASCADE, verbose_name='所属交易场所', blank=False, null=False, help_text='子公司所属集团')
    is_activate = models.BooleanField(default=True, verbose_name='状态', blank=True, null=True, help_text='该公司是否继续使用')
    company_code = models.CharField(max_length=10, verbose_name='子公司代码', blank=True, null=True, help_text='子公司代码', default='')

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
    is_activate = models.BooleanField(default=True, verbose_name='状态', blank=True, null=True, help_text='该分类是否继续使用')

    class Meta:
        verbose_name = '经营分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Products(models.Model):
    """
    商品表
    """
    scope = models.ForeignKey(BusinessScope, on_delete=models.CASCADE, verbose_name='分类', blank=False, null=False, help_text='大的经营分类')
    name = models.CharField(max_length=40, verbose_name='商品名称', blank=False, null=False, help_text='商品名称')
    type = models.CharField(max_length=511, verbose_name='商品型号', blank=False, null=False, help_text='商品型号')
    price_min = models.PositiveIntegerField(verbose_name='单价下限', help_text='单价下限(元)', blank=False, null=False)
    price_max = models.PositiveIntegerField(verbose_name='单价上限', help_text='单价上限(元)', blank=False, null=False)
    unit = models.CharField(max_length=40, verbose_name='计量单位', blank=False, null=False, help_text='计量单位')
    total_range = models.CharField(choices=settings.TOTAL_RANGE, max_length=3, verbose_name='单笔定金范围', blank=False, null=False, help_text='单笔定金范围')
    is_activate = models.BooleanField(default=True, verbose_name='状态', blank=True, null=True, help_text='该商品是否继续使用')

    class Meta:
        verbose_name = '商品表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BusinessCompany(models.Model):
    """
    交易公司表
    """
    name = models.CharField(max_length=100, verbose_name='企业名称', blank=False, null=False, help_text='企业名称')
    scope = models.ForeignKey(BusinessScope, on_delete=models.CASCADE, verbose_name='企业经营分类', blank=False, null=False, )
    corporation = models.CharField(max_length=20, verbose_name='企业法人姓名', blank=True, null=True, help_text='企业法人姓名')
    registered_capital = models.IntegerField(verbose_name='企业注册资金(元)', blank=True, null=True, help_text='企业注册资金')
    registered_capital_currency = models.CharField(max_length=10, verbose_name='注册资金币种', blank=True, null=True, help_text='注册资金币种', default='元人名币')
    registered_province = models.CharField(max_length=15, verbose_name='注册省份', blank=True, null=True, help_text='注册省份')
    telphone = models.CharField(max_length=15, verbose_name='企业办公电话', blank=True, null=True, help_text='企业办公电话')
    is_activate = models.BooleanField(default=True, verbose_name='状态', blank=True, null=True, help_text='该公司是否继续使用')

    class Meta:
        verbose_name = '交易公司'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Buyer(BusinessCompany):
    """
    买方表
    """
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='所属集团子公司')
    mouth_buy_limit = models.PositiveSmallIntegerField(verbose_name='每月交易上限', blank=True, null=True, default=5, help_text='买方每月交易笔数上限')
    total_range = models.CharField(choices=settings.TOTAL_RANGE, max_length=1, verbose_name='单笔定金范围', blank=False, null=False, help_text='单笔定金范围')
    
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
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='所属集团子公司')
    account_name = models.CharField(max_length=40, verbose_name='账号名称', blank=True, null=True, help_text='账号名称')
    account = models.CharField(max_length=40, verbose_name='账号', blank=True, null=True, help_text='账号')
    bank_name = models.CharField(max_length=40, verbose_name='开户行名称', blank=True, null=True, help_text='开户行名称')
    bank_code = models.CharField(max_length=40, verbose_name='开户行联行号', blank=True, null=True, help_text='开户行联行号')
    is_activate = models.BooleanField(default=True, verbose_name='状态', blank=True, null=True, help_text='该账户是否使用')
    is_corporate = models.BooleanField(default=False, verbose_name='是否对公户', blank=True, null=True, help_text='该账户是否是对公户, 勾选代表是对公户, 取消勾选代表是单位结算卡(默认)')

    class Meta:
        verbose_name = '账号'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.account_name
