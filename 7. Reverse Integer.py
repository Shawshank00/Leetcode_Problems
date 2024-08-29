class Solution:
    def reverse(self, x: int) -> int:
        a = abs(x)
        rev = 0
        z = 1

        while a > 0:    
            rev = rev*10 + a % 10
            a = a // 10
        
        if x >= 0 and rev < 2**31:
            return rev
        elif x < 0 and rev <= 2**31:
            return 0 - rev
        else:
            return 0
