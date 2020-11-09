ilk = int(input("Enter the first number: "))
ikinci = int(input("Enter the second number: "))
toplam =str( ilk + ikinci)
basamak= len(toplam)

liste1= []
if (basamak <2):
  print("0",toplam)
elif (basamak>=2):
  yeni_toplam = toplam[:: -1]
  print(yeni_toplam[0:2 -1])

  


