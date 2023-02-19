s = "abcde"
goal = "cdeas"
count = 0

if(len(s) != len(goal)):
    print(False)
    # return False
for loop in range(0,2):
    for i in range(0, len(s)):
        if(s[i] != goal[count]):
            count = 0
        if(s[i] == goal[count]):
            print(s[i],goal[count])
            count += 1
            
        if(i == len(goal)):
            i = 0
        if(count == len(goal)):
            print(True)
            # return True

print(False)
# return False
        

