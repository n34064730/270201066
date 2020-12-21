def get_evens(liste,counter=0):
  if len(liste)==0:
    return counter 

  if liste[0]%2==0:
    counter+=1
    print("hey")
    return get_evens(liste[1:])
  elif liste[0]%2!=0:
    liste.pop(0)
    return get_evens(liste)
  

x=get_evens([1,2,3,4])
print(x)