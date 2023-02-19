import math
x = 1298015993

if(x == 0):
    return 0
if(x == 1):
    return 1
if(x == 2):
    return 1

for i in range(1, x):
    value = math.floor(x / i)
    # print(value, i)
    if (value == i or value == i-1):
        # print(value)
        return value
        break