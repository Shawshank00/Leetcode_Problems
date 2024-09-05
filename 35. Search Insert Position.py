class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
       
        '''
        #Solution 1: Bruteforce
        n = 0
        for i in range(len(nums)):
            if nums[i] < target:
                n += 1
        return n
        #TC - O(n)
        #SC - O(1)
        '''
        
        #Solution 2: Optimal

        L, R = 0, len(nums)

        while L < R:
            M = L + ((R-L) // 2)

            if nums[M] < target:
                L = M + 1
            else:
                R = M
        return L

        #TC - O(log n)
        #SC - O(1)

