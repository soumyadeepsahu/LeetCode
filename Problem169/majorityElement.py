nums = [1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,3,3,3,3,3,3,333,33,3,3,3,3,3,3,3,3,3,3]
count = 1
# maxCount = 0
maxNum = nums[0]

for i in range(len(nums)):
    if(maxNum == nums[i]):
        count += 1
    else:
        count -= 1
    if(count == 0):
        maxNum = nums[i]
        count = 1
        
print(maxNum)


