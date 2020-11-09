ilk = int(input("Enter the first number: "))
ikinci = int(input("Enter the second number: "))
toplam =str( ilk + ikinci)
basamak= len(toplam)

liste1= []
if (basamak <2):
  sonuc = "0"+toplam
  print(sonuc)
elif (basamak>=2):
  yeni_toplam = toplam[:: -1]
  sona_gelelimartik = yeni_toplam[0:2]
  print(sona_gelelimartik[:: -1])


  


