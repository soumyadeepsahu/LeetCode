strs = ["abafa","ab","abvd","abafa"]

        
a = strs[0]
b = ""

if len(strs) == 1:
    print(a)

for i in strs:
    if a == "":
        print(a)  

    if a != i:
        for j in range(len(i)):
            if a[j] == i[j]: 
                b += i[j]
        c = b            
        b = ""               
    else:
        continue

print(c)
               
    




# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         a = strs[0]
#         b = ""

#         if len(strs) == 1:
#             return a

#         for i in strs:
#             if a == "":
#                 return a  

#             if a != i:
#                 for j in range(len(i)):
#                     if a[j] == i[j]: 
#                         b += i[j]
#                 c = b            
#                 b = ""               
#             else:
#                 continue

#         return c
           
            
                     

                        
                   