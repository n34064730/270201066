liste = []
degerler = input("Enter the values (for exit type quit) :")
while degerler != "quit":
  sayilar = int(degerler)
  liste.append(sayilar)
  degerler = input("Enter the values (for exit type quit) :")
sonuc = set(liste)
print(sonuc)