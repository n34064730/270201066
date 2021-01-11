def multp3(number,c=3):
  if c==0:
    return 0
  return number + multp3(number,c-1)
print(multp3(8))