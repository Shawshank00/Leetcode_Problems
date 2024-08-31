class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        S = set()
        count = 0

        for i in nums:
            if i in S:
                count += 1
            else:
                S.add(i)
            
            if count == 1:
                return True
                break
        return False
