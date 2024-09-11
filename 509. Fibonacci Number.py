class Solution:
    def fib(self, n: int) -> int:
        
        prev1 = 0
        prev2 = 1
        fib = 0
        if n == 0: return 0
        elif n == 1: return 1
        else:
            for i in range(2,n+1):
                fib = prev1 + prev2
                prev1 = prev2
                prev2 = fib
            return fib
