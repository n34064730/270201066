def ss(liste):
  min=9999999999999
  max=0
  new_list=[]

  for i in liste:
    if i<min:
      min=i
      liste.remove(i)
      new_list.append(min)
  new_list[::-1]
  for x in liste:
    if x>new_list[-1]:
      new_list.append(x)




print(ss([101,8,88]))
""""    
def selSort(nums):
    # sort nums into ascending order
    n = len(nums)

    # For each position in the list (except the very last)
    for bottom in range(n - 1):
        # find the smallest item in nums[bottom]..nums[n-1]
        mp = bottom  # bottom is smallest initially
        for i in range(bottom + 1, n):  # look at each position
            if nums[i] < nums[mp]:  # this one is smaller
                mp = i  # remember its index
        # swap smallest item to the bottom
        nums[bottom], nums[mp] = nums[mp], nums[bottom]"""