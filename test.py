from Tran.utils import hongbao

def test2():
  nums = 0
  while True:
      if nums > 10:
          return 
      nums += 1
      hongbao_list = hongbao(total=2146, num=4)
      # print('-hongbao_list--')
      # print(hongbao_list)
      if (max(hongbao_list) < 950) and (min(hongbao_list) > 50):
          return hongbao_list


def test():
  for i in range(100):
    hongbao_list = test2()
    if max(hongbao_list) > 950 or min(hongbao_list) < 50:
      print(sum(hongbao_list))
      print(hongbao_list)
      print('-------')