#1. using for loop: #O(n) & O(1)

class Solution:
    def climbStairs(self, n: int) -> int:
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

#2. using Top down memorisation: #O(n) & O(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2}
        def f(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = f(n-1) + f(n-2)
                return memo[n]
        return f(n)

#3. using Bottom up tabulation: #O(n) & O(n)

class Solution:
    def climbStairs(self, n: int) -> int:

        arr = [0] * n
        arr[0] = 1
        arr[1] = 2

        for i in range(2,n):
            arr[i] = arr[i-1] + arr[i-2]
        return arr[n-1]
