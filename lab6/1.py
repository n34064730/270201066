e_mail = "ceng113@example.com"
einput = input("E mail: ")
mail1 = einput.lower()

mail2 = mail1.replace(".","")
if mail2== e_mail:
  print("True")
else:
  print("Wrong")