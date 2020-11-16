num1 = input("Enter a positive number: ")
num2 = input("Enter a positive number: ")
count = 0
x=0
for i in num1:
  if i in num2:
    count+=1
for i in num2:
  if i in num1:
    x +=1
if (x>= count):
  print(x)      
else:
  print(count)    
