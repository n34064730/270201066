def harmonic(num):
  if num==1:
    return 1
  return 1/num + harmonic(num-1)

x=int(input("Enter the num: "))
print(harmonic(x))