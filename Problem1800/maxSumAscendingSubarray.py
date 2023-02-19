nums = [5,5,6,6,6,9,1,2]
max = nums[0]
sum = nums[0]

for i in range(1,len(nums)):
    if(nums[i-1] < nums[i]):
        sum += nums[i]
    if(sum > max):
        max = sum
    if(nums[i-1] >= nums[i]):
        sum = nums[i]
    print(sum)
print(max)        