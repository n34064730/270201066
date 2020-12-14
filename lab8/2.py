def prime(number):
  if number==2:
    return True
  else:
    for i in range(2,number):

      if number%i==0:
        return False
      else:
        return True
number=int(input("Enter number: "))
if prime(number):
  print("{} is a prime number".format(number))
else:
  print("{} is not a prime number".format(number))
