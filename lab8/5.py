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
        ysayac+=1
      elif i.isprintable():
        zsayac+=1
  if(space!=0):
    return("{}\t(Level 0)".format(password))
  elif((xsayac!=0)and(ysayac!=0)and(zsayac!=0)):
    return("{}\t(Level 3)".format(password))
  elif((xsayac!=0 and ysayac!=0 and zsayac==0)or(xsayac!=0 and zsayac!=0 and ysayac==0)or(ysayac!=0 and zsayac!=0 and xsayac==0)):
    return("{}\t(Level 2)".format(password))
  elif((xsayac !=0 and ysayac==0 and zsayac==0)or(xsayac==0 and ysayac!=0 and zsayac==0)or(xsayac==0 and ysayac==0 and zsayac!=0)):
    return("{}\t(Level 1)".format(password))
password=input("Enter password:")
print(password_checker(password))    

