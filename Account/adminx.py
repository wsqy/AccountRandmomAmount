import xadmin
from django.utils.html import format_html
from xadmin.models import Log

from .models import Company, BusinessScope, BusinessCompany, Buyer, Seller, Account, Products

class BaseSetting:
    enable_themes = True
    use_bootswatch = True


class GlobalSettings:
    # 站点标题
    site_title = '转账生成系统管理后台'
    # 站点底部显示问题
    site_footer = '-- wsqy --'
    # 设置菜单可折叠
    menu_style='accordion'


class AccountInline:
    model = Account
    extra = 1


class CompanyAdmin:
    list_display = ['name', 'corporation', 'is_activate',]
    list_filter = ['corporation', 'is_activate',]
    list_editable = ['name',]
    search_fields = ['name',]    
    import_excel = True
    inlines = [AccountInline, ]
    model_icon = 'fa fa-credit-card'


class BusinessScopeAdmin:
    list_display = ['id', 'name', 'is_activate']
    list_display_links = ['id', 'name']
    list_editable = ['name', 'is_activate']
    search_fields = ['name',]
    list_filter =['is_activate',]
    model_icon = 'fa fa-credit-card'


class ProductsAdmin:
    list_display = ['id', 'name','scope', 'type', 'price_min', 'price_max', 'unit', 'total_range', 'is_activate',]
    list_display_links = ['id', 'name']
    list_editable = ['scope', 'name', 'type', 'price_min', 'price_max', 'unit', 'total_range', 'is_activate',]
    list_filter = ['scope','total_range', 'is_activate',]
    search_fields = ['name', 'type',]    
    model_icon = 'fa fa-credit-card'


class BusinessCompanyAdmin:
    list_display = ['id', 'name', 'scope', 'registered_province']
    list_editable = ['scope', ]
    list_filter = ['scope', 'is_activate',]
    search_fields = ['name', 'corporation', 'registered_province']
    model_icon = 'fa fa-credit-card'


class AccountAdmin:
    list_display = ['company', 'account_name', 'account', 'bank_name', 'bank_code']
    search_fields = ['company', 'account', 'bank_name', 'bank_code']
    import_excel = True
    model_icon = 'fa fa-credit-card'


class BuyerAdmin:
    list_display = ['name', 'scope', 'company', 'day_total_max_limit',
                    'mouth_total_max_limit', 'is_activate', ]
    list_editable = ['scope', 'day_total_max_limit', 'mouth_total_max_limit']
    search_fields = ['name',]
    # inlines = [AccountInline, ]
    model_icon = 'fa fa-credit-card'


class SellerAdmin:
    list_display = ['id', 'name', 'scope', 'registered_province']
    list_editable = ['scope', ]
    list_filter = ['scope', 'is_activate', 'registered_province']
    search_fields = ['name', 'corporation', 'registered_province']
    model_icon = 'fa fa-credit-card'


xadmin.site.unregister(Log)
xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
xadmin.site.register(Company, CompanyAdmin)
xadmin.site.register(BusinessScope, BusinessScopeAdmin)
xadmin.site.register(Products, ProductsAdmin)
xadmin.site.register(Buyer, BuyerAdmin)
xadmin.site.register(Seller, SellerAdmin)
xadmin.site.register(Account, AccountAdmin)