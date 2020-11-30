import string
numbers = str(range(0,10))
lower_cases =list(string.ascii_lowercase)
upper_cases = list(string.ascii_uppercase)
i = 0; j=0; k=0

while True: 

  password = input("Enter a password\nfor exit type'exit :")
  if password == "exit":
    break
  if len(password)>=8:
    for x in password:
      if x in lower_cases:
        i+=1
        print(i,x)
      if x in upper_cases:
        j +=1
        print(j,x)
      if x in numbers:
        print(k,x)
        k+= 1
    if ((i>0)and(j>0)and(k>0)):
      print("True")
    else:
      print("Wrong")
      
      
  else:
    print("Wrong")
    
