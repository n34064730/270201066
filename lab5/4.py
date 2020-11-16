p1 = input("Enter the password: ")

while True:
  p2 = input("Enter password again: ")
  if p2 == "help":
    print(p1[0])
  elif p1 == p2:
    print("Welcome")
    break
  else:
    print("Wrong")    