months = "january, february, \nmarch , april ,may, jun , \njuly ,august, september, october , november , december"
print(months)
month = int(input("Which month are you on? \n choose from the list as numbers \n(for instance january is 1, february is 2 "))
day= int(input("Which day are you at :"))
if (((month == 4) and(day >=20)) or (4<month<6 ) or ((month == 6) and (day < 21))):
  print("It is spring")
elif (((month == 6) and(day >=21)) or (6<month<8 ) or ((month == 9) and (day < 22))):
  print("It is summer")
elif (((month == 9) and(day >=22)) or (9<month<11 ) or ((month == 12) and (day < 21))):
  print("It is fall")    
elif (((month == 12) and(day >=21)) or (1<=month<3 ) or ((month == 4) and (day < 20))):
  print("It is winter")  