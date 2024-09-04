class Solution:
    def findMissingRepeatingNumbers(self, nums):
        
        n = len(nums)
        act_nums = int(n * (n + 1) / 2)
        arr = set()
        sum_nums = 0
        for i in nums:
            sum_nums += i
            if i in arr:
                twice = i
            else:
                arr.add(i)
        return twice, abs(act_nums + twice - sum_nums)

      #Time Complexity:O(n) due to the single loop for traversing nums
      #Space Complexity:O(n) for the set to store unique numbers
