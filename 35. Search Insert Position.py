class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = 0
        for i in range(len(nums)):
            if nums[i] < target:
                n += 1
        return n
