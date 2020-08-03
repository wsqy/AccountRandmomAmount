from Account.models import Buyer, Seller, Account
import random

def get_random(min, max):
    _list =  [i*100 for i in range(min, max)]
    return _list + [0 for i in range(30)]
    


# def create_seller():
#     _mouth = get_random(199, 777)
#     _day = get_random(22,122)
#     for i in range(400):
#         Seller.objects.create(name="卖方公司{}".format(i+111), scope_id=8,
#               is_activate=True, mouth_total_max_limit=random.choice(_mouth),
#               day_total_max_limit= random.choice(_day))


def create_seller():
    buyer_list = Buyer.objects.all()
    for buyer in buyer_list:
        buyer.name = '买' + buyer.name[1:]
        buyer.save()