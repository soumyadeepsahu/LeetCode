class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:    
            y = int(0)
            temp = x 
            while temp >= 10:
                y += int(temp % 10)
                y *= int(10)
                temp /= int(10)

            y += int(temp)

            if y == x:
                return True
            else: 
                return False