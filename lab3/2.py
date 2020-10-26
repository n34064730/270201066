ilk = int(input("İlk sayıyı girin: "))
iki = int(input("İkinci sayıyı girin: "))
uc = int(input("Üçüncü sayıyı girin: "))
if( (ilk<= iki)    and (ilk <= uc)      ):
  print("En küçük sayı : ",ilk)
elif((iki <= ilk) and (iki<= uc)):
  print("En küçük sayı : ",iki)
elif((uc <= iki) and (uc<= ilk)):
  print("En küçük sayı : ",uc)
