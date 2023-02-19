import array as arr

nums = arr.array('i', [-1,0,0,0,0,3,3])
lastNum = -101;
skipperCount = 0;
k = 0

for i in range(len(nums)):
    if(nums[i]==lastNum):
        skipperCount += 1
    if(nums[i]!=lastNum):
        k += 1    
    nums[i-skipperCount] = nums[i]
    lastNum = nums[i]

print(nums,k)    