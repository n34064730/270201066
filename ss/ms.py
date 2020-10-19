#1'den 1000'e kadar mükemmel sayıları yazdıran fonksiyon
#mükemmel sayı bölenlerinin toplamı kendisine eşit sayı

def perfect(number):
  toplam = 0
  
  for i in sayı:
    if (sayı % i == 0):
      
      toplam += i
      return toplam == number
  

for i in range (1, 1001):
  if (perfect(i)):
    print("mükemmel",i)