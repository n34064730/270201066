def harmonic(num):
  toplam=0
  for i in range(1,num+1):
    toplam+=1/i
  return toplam
x=int(input("Enter the num: "))
print(harmonic(x))