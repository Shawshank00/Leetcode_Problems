class Solution:
    def climbStairs(self, n: int) -> int:

        #This is fib series if visualized:
        prev1 = 2
        prev2 = 3
        count = 0
        if n <= 3:
            return n
        else:
            for i in range(4, n+1):
                count = prev1 + prev2
                prev1 = prev2
                prev2 = count
            return count
                
        
