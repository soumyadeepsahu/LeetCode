n = 5
ways = 0
temp1 = 1
temp2 = 2

if(n >= 2):
    for i in range(1, n):
        ways = temp1 + temp2
        temp1 = temp2
        temp2 = ways 
        # print(ways)
else:
    pass
    # return 1
        