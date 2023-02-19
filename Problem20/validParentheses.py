s = "()"

stackOpen = []
stackClose = []

for i in range(len(s)):
    if(s[i] == "(" or s[i] == "{" or s[i] == "["):
        stackOpen.append(s[i])
    elif(s[i] == ")" or s[i] == "}" or s[i] == "]"):
        stackClose.append(s[i])

    if(len(stackOpen) > 0 and len(stackClose) > 0):
        if(stackOpen[len(stackOpen)-1] == "(" and stackClose[len(stackClose)-1] == ")" 
        or stackOpen[len(stackOpen)-1] == "{" and stackClose[len(stackClose)-1] == "}"
        or stackOpen[len(stackOpen)-1] == "[" and stackClose[len(stackClose)-1] == "]"):
            if(s[i-1] == stackClose[len(stackClose)-1] and s[i] == stackOpen[len(stackOpen)-1]):
                pass
            else:
                stackOpen.pop()
                stackClose.pop()
        else:
            pass
    
if(len(stackOpen) or len(stackClose) != 0):
    # print(stackOpen)
    # print(stackClose)
    print(False)
else:
    print(True)
    

    





























# counterRound = 0
# counterCurly = 0
# counterSquare = 0

# counterRoundEnd = 0
# counterCurlyEnd = 0
# counterSquareEnd = 0


# for i in range(len(s)):
#     if (s[i] == "("):
#         counterRound += 1
#     if (s[i] == "{"):
#         counterCurly += 1
#     if (s[i] == "["):
#         counterSquare += 1
#     if (s[i] == ")"):
#         counterRoundEnd += 1
#     if (s[i] == "}"):
#         counterCurlyEnd += 1
#     if (s[i] == "]"):
#         counterSquareEnd += 1

#     if i != len(s)-1:
#         if (s[i] == s[i+1]):
#             pass
#         elif (s[i] == "(" and s[i+1] != ")" ):
#             print ("a",s[i+1])
#         elif (s[i] == "{" and s[i+1] != "}" ):
#             print ("b",s[i+1])
#         elif (s[i] == "[" and s[i+1] != "]" ):
#             print ("c",s[i+1])



# class Solution:
#     def isValid(self, s: str) -> bool:
#         counterRound = 0
#         counterCurly = 0
#         counterSquare = 0

#         counterRoundEnd = 0
#         counterCurlyEnd = 0
#         counterSquareEnd = 0


#         for i in range(len(s)):
#             if (s[i] == "("):
#                 counterRound += 1
#             if (s[i] == "{"):
#                 counterCurly += 1
#             if (s[i] == "["):
#                 counterSquare += 1
#             if (s[i] == ")"):
#                 counterRoundEnd += 1
#             if (s[i] == "}"):
#                 counterCurlyEnd += 1
#             if (s[i] == "]"):
#                 counterSquareEnd += 1



#             if i != len(s)-1:
#                 if (s[i] == s[i+1]):
#                     pass
#                 elif (s[i] == "(" and s[i+1] != ")" ):
#                     return False
#                 elif (s[i] == "{" and s[i+1] != "}" ):
#                     return False
#                 elif (s[i] == "[" and s[i+1] != "]" ):
#                     return False


#         if (counterRound == counterRoundEnd):
#             pass
#         else:
#             return False

#         if (counterSquare == counterSquareEnd):
#             pass
#         else:
#             return False

#         if (counterCurly == counterCurlyEnd):
#             pass
#         else:
#             return False 

#         return True 