e_mail = "ceng113@example.com"
einput = input("E mail: ")
mail1 = einput.lower()
mail1 = mail1.split("@")


mail2 = mail1[0].replace(".","")
if mail2== e_mail:
  print("True")
else:
  print("Wrong")