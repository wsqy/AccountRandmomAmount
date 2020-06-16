import xadmin
from django.utils.html import format_html

from .models import DayBuyer, DaySeller, MouthBuyer, MouthSeller


class DayBuyerAdmin:
    list_display = ['date', 'buyer', 'amount_total']
    list_filter = ['date', 'buyer']

    def has_add_permission(self):
        return False

class DaySellerAdmin:
    list_display = ['date', 'seller', 'amount_total']
    list_filter = ['date', 'seller']

    def has_add_permission(self):
        return False

class MouthBuyerAdmin:
    list_display = ['mouth', 'buyer', 'amount_total']
    list_filter = ['mouth', 'buyer']

    def has_add_permission(self):
        return False

class MouthSellerAdmin:
    list_display = ['mouth', 'seller', 'amount_total']
    list_filter = ['mouth', 'seller']

    def has_add_permission(self):
        return False

xadmin.site.register(DayBuyer, DayBuyerAdmin)
xadmin.site.register(DaySeller, DaySellerAdmin)
xadmin.site.register(MouthBuyer, MouthBuyerAdmin)
xadmin.site.register(MouthSeller, MouthSellerAdmin)