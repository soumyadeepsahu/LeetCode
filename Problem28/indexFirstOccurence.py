haystack = "mississippi"
needle = "issip"

ini = -1
count = 0
j = 0

if(len(haystack)<len(needle)):
    print(ini)

for i in range(len(haystack)):
    if(haystack[i] == needle[j]):
        count += 1
        if(j == 0):
            ini = i
    if(haystack[i] != needle[j]):
        count = 0
        j = 0
        ini = -1

    if(count == len(needle)):
        print(haystack[ini])
        print(ini)
        break
    print(count)
    j = count


# print(ini)  
       
