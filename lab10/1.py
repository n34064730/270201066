def liste(number):
  liste=[]
  for i in range(4):
    liste.append(number)
  return liste
  
def mult(liste):
  if len(liste)==0:
    return 0
  return liste[0]+liste[1:]

