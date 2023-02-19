jewels = "aAFD" 
stones = "aAAbbbbfsafdehgsGADGDFVNTHCASDdsfsFASBEF"
count = 0

for i in range(0, len(stones)):
    for j in range(0, len(jewels)):
        if(stones[i] == jewels[j]):
            count += 1

print(count)
# return count