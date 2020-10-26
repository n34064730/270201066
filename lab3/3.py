gpa = int(input("Enter the gpa :"))
lec= int(input("Enter the number of lecture :"))
if ((gpa< 2.0) and (lec < 47)):
  print("Not enough number of lectures and GPA")
elif ((gpa < 2.0) and (lec >= 47)):
  print("Not enough GPA!")
elif((gpa >= 2.0) and (lec < 47) ):
  print("Not enough number of lectures!")
elif( (gpa>= 2.0) and (lec >= 47)):
  print("GRADUATED, but at what cost")      
