liste = []
deger = int(input("Enter value for exit type 'q':"))
cikis = str(deger)

while cikis != "q":
  
  liste.append(deger)
  deger = int( input("Enter value for exit type 'q':"))
  cikis = str(deger)
set1 = set(liste)
print(set1)