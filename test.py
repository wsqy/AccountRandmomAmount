import random
import collections
from Account.models import Seller, Company

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

if __name__ == '__main__':
    random_choice_scale()

