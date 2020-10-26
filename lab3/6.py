print("a b ve c değerlerini gösterildiği girin \n ax**2+bx+c")
a= float(input("a değerini girin:"))
b = float(input("b değerini girin:"))
c = float(input("c değerini girin:"))
ucgen = ((b**2) - 4*a*c)
if (ucgen > 0 ):
  kok1 = ((-b * ucgen**(-1/2)) / (2*a))
  kok2 = ((-b * ( (-1) * ucgen**(-1/2))) / (2*a))
  print("Kökler reel sayılardadır ve 2 tanedir bunlar :  {} {}".format(kok1,kok2))
elif (ucgen == 0):
  kok =  ((-b * ucgen**(-1/2)) / (2*a))
  print("Denklemin tek kökü var o da ",kok)
else:   
  kok1 = ((-b * ucgen**(-1/2)) / (2*a))
  kok2 = ((-b * ( (-1) * ucgen**(-1/2))) / (2*a))
  print("Kökleriniz irrasyonel ve {} {} ".format(kok1,kok2))