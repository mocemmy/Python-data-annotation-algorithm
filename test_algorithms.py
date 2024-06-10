# def create_staircase(nums):
#   while len(nums) != 0:
#     step = 1
#     subsets = []
#     if len(nums) >= step:
#       subsets.append(nums[0:step])
#       nums = nums[step:]
#       step += 1
#     else:
#       return False

#   return subsets

def create_staircase(nums):
  step = 1
  subsets = []
  while len(nums) != 0:
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False
      
  return subsets

print('test 1: possible', create_staircase([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print('test 2: impossible', create_staircase([1, 2, 3, 4]))