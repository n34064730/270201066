def get_evens(liste,counter=0):
  if len(liste)==0:
    return counter 
  if liste[0]%2==0:
    return get_evens(liste[1:],counter+1)
  elif liste[0]%2!=0:
    return get_evens(liste[1:],counter)
  

x=get_evens([1,2,3,4,8])
print(x)