class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        arr = []
        i = 0
        
        while i < len(nums):
            cur = nums[i]
            
            while i < len(nums)-1 and nums[i+1] == nums[i] + 1:
                i = i + 1
            
            if cur == nums[i]:
                arr.append(str(cur))
            else:    
                arr.append(str(cur) + '->' + str(nums[i]))
            i = i + 1
        
        return arr

        
