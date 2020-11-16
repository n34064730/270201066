num1 = input("Enter a positive number: ")
num2 = input("Enter a positive number: ")
count = 0
num = set()
numm = set()
x=0
for i in num1:
  num.update(i) 
for i in num2:
  numm.update(i) 
for i in num:
  if i in numm:
    count+=1
for i in numm:
  if i in num:
    x +=1
if (x>= count):
  print(x)      
else:
  print(count)    
