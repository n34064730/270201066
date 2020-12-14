a_list = [12, -7, 5, -89.4, 3, 27, 56, 57.3]
def toplam(number):
  toplam=0
  number=abs(number)
  for i in range(int(number)+1):
    toplam+=i
  print(toplam**2)
  
for i in a_list:
  toplam(i)
