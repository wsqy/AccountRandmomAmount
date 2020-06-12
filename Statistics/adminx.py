import xadmin
from django.utils.html import format_html

from .models import DayBuyer, DaySeller, MouthBuyer, MouthSeller


class DayBuyerAdmin:
    def has_add_permission(self):
        return False

class DaySellerAdmin:
    def has_add_permission(self):
        return False

class MouthBuyerAdmin:
    def has_add_permission(self):
        return False

class MouthSellerAdmin:
    action_on_bottom = False
    def has_add_permission(self):
        return False

xadmin.site.register(DayBuyer, DayBuyerAdmin)
xadmin.site.register(DaySeller, DaySellerAdmin)
xadmin.site.register(MouthBuyer, MouthBuyerAdmin)
xadmin.site.register(MouthSeller, MouthSellerAdmin)