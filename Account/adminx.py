import xadmin
from django.utils.html import format_html
from xadmin.models import Log

from .models import Company, BusinessScope, BusinessCompany, Buyer, Seller, Account

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

class CompanyAdmin:
    list_display = ['name', 'corporation', 'is_activate',]
    list_filter = ['corporation', 'is_activate',]
    list_editable = ['name',]
    search_fields = ['name',]    
    import_excel = True

class BusinessScopeAdmin:
    list_display = ['id', 'name',]
    list_editable = ['name',]
    search_fields = ['name',]

class BusinessCompanyAdmin:
    list_display = ['id', 'name',]
    list_editable = ['name',]
    search_fields = ['name',]

class BusinessCompanyInline:
    model = BusinessCompany
    extra = 1


class AccountInline:
    model = Account
    extra = 1

class AccountAdmin:
    list_display = ['businesscompany', 'account_name', 'account', 'bank_name', 'bank_code']
    # list_editable = ['scope', 'total_max_limit']
    search_fields = ['businesscompany', 'account', 'bank_name', 'bank_code']
    import_excel = True

class BuyerAdmin:
    list_display = ['name', 'scope', 'is_activate', 'total_max_limit', 'company']
    list_editable = ['scope', 'total_max_limit']
    search_fields = ['name',]
    inlines = [AccountInline, ]

class SellerAdmin:
    list_display = ['name', 'scope', 'is_activate', 'total_max_limit', ]
    list_editable = ['scope', 'total_max_limit']
    search_fields = ['name',]
    inlines = [AccountInline, ]

xadmin.site.unregister(Log)

xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
xadmin.site.register(Company, CompanyAdmin)
xadmin.site.register(BusinessScope, BusinessScopeAdmin)
xadmin.site.register(Seller, SellerAdmin)
xadmin.site.register(Buyer, BuyerAdmin)
xadmin.site.register(Account, AccountAdmin)