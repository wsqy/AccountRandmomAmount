from Account.models import Seller

def test():
  with open('橡塑隐藏取消.txt',) as f:
    for (i,line) in enumerate(f.readlines(), 1):
      # print("%s %s" % (i, line))
      Seller.objects.filter(name=line.strip('\n').strip()).update(is_activate=False)

