def hailstone(number,liste=[]):
  if number==1:
    liste.append(1)
    lis=str(liste);lis=lis.replace("[","");lis=lis.replace("]","")
    print(lis)
    return 0
  elif number %2 ==0:
    liste.append(int(number))
    number=number/2
    return hailstone(number,liste)
  elif number %2 ==1:
    liste.append(int(number))
    number=3*number+1
    return hailstone(number,liste)

hailstone(11)

hailstone(5,[])
#If I don't use [] after first usage, it won't display as we wanted