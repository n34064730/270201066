age = int(input("How old are you citizen :"))
ticket = 3.0
if ((age < 6 ) or (age >60)):
  ticket = 0
  print("Price of the ticket is: ",ticket) 
elif (6<=age<=18):
  ticket = ticket * 0.5
  print("Price of the ticket is: ",ticket) 
else:
  print("Price of the ticket is: ",ticket)    
