class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        arr = [0] * len(nums)
        p, n = 0 , 1

        for i in nums:
            if i >= 0:
                arr[p] = i
                p += 2
            else:
                arr[n] = i
                n += 2
        return arr

        #Time Complexity:O(n) where n is the length of nums due to a single pass through the list
        #Space Complexity:O(n) for the temporary array arr to hold rearranged elements
