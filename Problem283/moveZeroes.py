nums = [0]
skipperCount = 0
k = 0

for i in range(len(nums)):
    if(nums[i] == 0):
        skipperCount += 1
    else:
        nums[i-skipperCount] = nums[i]
        k += 1

for i in range(k, len(nums)):
    nums[i] = 0

print(nums)