import array as arr

nums = arr.array('i', [2,0,1,2,2,3,0,4,2])
delNum = 2
skipperCount = 0
k = 0

for i in range(len(nums)):
    if(nums[i]==delNum):
        skipperCount += 1
        pass
    else:
        k += 1     
        nums[i-skipperCount] = nums[i]

print(nums,k)    