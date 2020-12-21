def get_reversed(liste):
  if len(liste)==0:
    return []
  return[liste[-1]]+get_reversed(liste[:-1])
liste=[1,2,3,4]
liste=get_reversed(liste)
print(liste)

