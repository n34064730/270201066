adet = int(input("How many numbers: "))
cift = 0
number = 0
for i in range(adet):
  number= int(input("Enter number "))
  if (number <0):
    print("Sadece pozitif sayıları girebilirsiniz !!!")
    
  elif number %2 ==0:
    cift +=1
sonuc = (cift/ adet)*100
print("%",sonuc)    