# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        L, R = 1, n

        while L < R:
            M = L + ((R-L) // 2)

            if isBadVersion(M):
                R = M
            else:
                L = M + 1
        return L

        #TC - O(log n)
        #SC - O(1)

