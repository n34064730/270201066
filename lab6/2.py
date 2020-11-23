ie = [[50,90,60],[15,60,75],[99,95,91]]
ilk = 0
ikinci = 0
ucuncu = 0
for i in ie[0]:
  ilk += i
for j in ie[1]:
  ikinci += j
for k in ie[2]:
  ucuncu += k
toplam = (ilk/3 * 0.3) + (ikinci/3 * 0.3)+ (ucuncu/3 * 0.4)
print(toplam)
