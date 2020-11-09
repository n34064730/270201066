ilk = int(input("Enter the first number: "))
ikinci = int(input("Enter the second number: "))
toplam = ilk + ikinci
if (toplam >= 100):
  print(toplam - 100)
elif(10<=toplam<100):
  print(toplam)
elif(0<=toplam<10):
  print("0",toplam)

