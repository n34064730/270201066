def binary(liste,number):
  if len(liste)>0:
    med=len(liste)//2
    if liste[med]==number:
      return med
    elif liste[med]>number:
      return binary(liste[:med],number)
    elif liste[med]<number:
      return binary(liste[med+1:],number)
  else:
    return ("element not in the list")
print(binary([1,2,3,5,77,4,85],85))
  