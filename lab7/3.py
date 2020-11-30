#Books cont
books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict = {}
for i in books:
  name = i
  sayi = len(name)
  uniqe = set()
  for x in name:
    uniqe.update(x)
  un_number = len(uniqe)
  avarage = (un_number + sayi)/2
  numbers = sayi,un_number,int(avarage)
  book_dict.update({name: numbers})

print(book_dict)