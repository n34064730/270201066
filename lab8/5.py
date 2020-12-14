def password_checker(password):
  if len(password)<8:
    return("{}\t(Level 0)".format(password))
  else:
    space=0
    xsayac=0
    ysayac=0
    zsayac=0
    
    for i in password:
      if i ==" ":
        space+=1
      elif i.isdigit():
        xsayac+=1
      elif i.isalpha():
        ysayac+=1:
      elif i.is.printable():
        zsayac+=1
  if(sapace=!0):
    return("{}\t(Level 0)".format(password))
  elif((xsayac!=0)or(ysayac!=0)or(zsayac!=0)):
    

