class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        arr = set(nums)
        cur_count = 0
        for i in nums:
            if i-1 not in arr:  #Needed to check for start of a sequence
                count = 0
                while i in arr:
                    count += 1
                    i += 1
                cur_count = max(cur_count, count)
        return cur_count

		#Time Complexity:O(n) where n is the number of elements in nums due to the set creation and the iteration through nums
		#Space Complexity:O(n) for the storage of the set containing the elements from nums
