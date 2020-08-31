import random
import collections
from Account.models import Seller, Company, Products

def get_company_list(corporation_id, num):
    def countX(company_list, company):
        count = 0
        for ele in company_list:
            if (ele.id == company.id):
                count = count + 1
        return count

    company_list = Company.objects.filter(is_activate=True, corporation__id=3).order_by('?')
    max_in = (num//company_list.count()) * 2
    new_company_list = []
    while True:
        if len(new_company_list) == num:
            return new_company_list
        company = random.choice(company_list)
        if countX(new_company_list, company) < max_in:
            new_company_list.append(company)
    return company_list


def test():
    # get_company_list(1, 3)
    for i in range(50):
      company_list = get_company_list(random.randint(1,7), random.randint(3,7))
      company_id_list = [company.id for company in company_list]
      print(collections.Counter(company_id_list))

def random_choice_scale():
    import time
    for i in range(10000):
        rand_data = int(time.time() * 10000000 % 38 + 12)
        if rand_data >50 or rand_data < 12:
            print(rand_data)
    print('ok')

def merge_quantity(amount, quantity, price):
    next_jisuan = 1
    for i in range(100):
        real_amount = round(quantity * price *0.3 / 10000, 1)
        if real_amount ==  amount:
            break
        elif real_amount <  amount:
            quantity += next_jisuan
        elif real_amount >  amount:
            if next_jisuan == 1:
                quantity -= 0.9
                next_jisuan = 0.1
            else:
                break
    print("数量: %s * 单价: %s, 应该是: %s, 实际是: %s" % (quantity, price, price*quantity, amount))


def merge_products():
    products_list = Products.objects.filter(is_activate=True).all()
    for products in products_list:
        _new_total_range = ''
        for _products in Products.objects.filter(is_activate=True, scope=products.scope, name=products.name, type=products.type,  unit=products.unit).order_by('total_range'):
            _new_total_range += _products.total_range
            _products.delete()
        products.total_range = _new_total_range
        products.save()


if __name__ == '__main__':
    merge_products()

