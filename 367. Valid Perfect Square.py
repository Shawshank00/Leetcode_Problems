class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        #Solution 1:
        
        L, R = 0, num - 1

        while L <= R:

            M = (L + R) // 2
            if M * M == num:
                return True
            elif M * M < num:
                L = M + 1
            else:
                R = M - 1
        return False
        
        '''
        #Solution 2:

        i = 1
        while i * i <= num:
            if i * i == num:
                return True
            else:
                i += 1
        return False
        '''
