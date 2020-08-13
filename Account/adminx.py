import xadmin
from django.utils.html import format_html
from xadmin.models import Log

from .models import Company, BusinessScope, BusinessCompany, Buyer, Seller, Account, Products, Corporation

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
    list_display = ['id', 'name', 'corporation', 'company_code', 'is_activate',]
    list_display_links = ['id', 'name']
    list_filter = ['corporation', 'is_activate',]
    list_editable = ['name', 'company_code']
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
    list_display = ['id', 'account_name', 'account', 'company', 'is_activate']
    list_display_links = ['id', 'account_name']
    search_fields = ['company', 'account', 'bank_code']
    list_filter = ['is_activate', 'company', ]
    # import_excel = True
    model_icon = 'fa fa-credit-card'


class BuyerAdmin:
    list_display = ['id', 'name', 'company', 'scope', 'mouth_buy_limit', 'total_range', 'is_activate']
    list_display_links = ['id', 'name']
    list_editable = ['scope', 'company', 'mouth_buy_limit', 'total_range', 'is_activate']
    list_filter = ['scope', 'is_activate', 'company', 'mouth_buy_limit', 'total_range', 'registered_province']
    search_fields = ['name', 'corporation', 'registered_province']
    model_icon = 'fa fa-credit-card'


class SellerAdmin:
    list_display = ['id', 'name', 'scope', 'is_activate']
    list_display_links = ['id', 'name']
    list_editable = ['scope', 'is_activate']
    list_filter = ['scope', 'is_activate', 'registered_province']
    search_fields = ['name', 'corporation', 'registered_province']
    model_icon = 'fa fa-credit-card'

class CorporationAdmin:
    list_display = ['id', 'name', 'template', 'is_activate']
    list_display_links = ['id', 'name',]
    list_editable = ['template', 'is_activate']
    list_filter = ['template', 'is_activate',]
    search_fields = ['name', 'template',]
    model_icon = 'fa fa-credit-card'

xadmin.site.unregister(Log)
xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
xadmin.site.register(Corporation, CorporationAdmin)
xadmin.site.register(Company, CompanyAdmin)
xadmin.site.register(BusinessScope, BusinessScopeAdmin)
xadmin.site.register(Products, ProductsAdmin)
xadmin.site.register(Buyer, BuyerAdmin)
xadmin.site.register(Seller, SellerAdmin)
xadmin.site.register(Account, AccountAdmin)