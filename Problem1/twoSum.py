nums = [2,7,11,15]

target = 9

for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    if j != len(nums)-1:
                        j += 1
                    else:
                        j = 0
                if nums[j]+nums[i] == target:
                    return i, j
