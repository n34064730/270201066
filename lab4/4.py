number = int(input("Enter the number "))
base = int(input("Enter the power "))
sonuc = 1
for i in range(1,base+1):
  sonuc *= number
print(sonuc)  