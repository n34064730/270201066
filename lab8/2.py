def is_prime(number):
  if number==2:
    return True
  else:
    for i in range(2,number):

      if number%i==0:
        return False
      else:
        return True
number=int(input("Enter number: "))
if is_prime(number):
  print("{} is a prime number".format(number))
else:
  print("{} is not a prime number".format(number))
def print_primes_between(number1,number2):
  liste=[]
  for i in range(number1+1,number2):
    if i==2:
      liste.append(i)
    else:
      for x in range(i):
        if i%x!=0:
          liste.append(i)
  return liste
number1=int(input("Enter the first number:"))
number2=int(input("Enter the second number:"))
print(print_primes_between(number1,number2))

      
    
      