adet = int(input("How many fibonacci numbers do you want to see: "))
sayac = 0
a=1
b=0
liste= []
while (adet> sayac):
  a= a+b
  a,b=b,a
  liste.append(b)
  sayac += 1
print(liste)