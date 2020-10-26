sayi = int(input("Sayıyı girin"))
mutlak_sayi = 0
# print("Girdiğiniz sayının mutlak değeri: ",abs(sayi))
if (sayi < 0 ):
  mutlak_sayi = sayi*(-1)
else:
  mutlak_sayi = sayi
print("Girmiş olduğunuz {} sayısının mutlak değeri {}".format(sayi,mutlak_sayi))  
