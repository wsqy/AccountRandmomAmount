from Account.models import Buyer
def test():
  for i in range(1,36):
    print("%s: " % i, end=' ')

    for j in [1,2,3]:
      print(Buyer.objects.filter(company__id=i, total_range=j).count(), end=' ')
    print()