class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        L, R = 0, len(nums) - 1

        while L <= R:
            M = L + ((R-L) // 2)

            if nums[M] == target:
                return M
            elif target < nums[M]:
                R = M - 1
            else:
                L = M + 1
        return -1

      # TC - O(log n)
      # SC - O(1)
