class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

# Simple Solution 1 - two for loops:
        for i in range(n-1):
            for j in range(i+1,n):
                if target == nums[i] + nums[j]:
                    return [i,j]
        return

# Solution 2 Optimal - using Hashmap and single loop:

        hashmap = {}
        for i in range(n):
            if target-nums[i] in hashmap:
                return [hashmap[target-nums[i]],i]
            else:
                hashmap[nums[i]] = i
        print(hashmap)
