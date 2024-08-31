class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = []
        left = 0
        right = len(nums) - 1

        while left <= right:
            
            if abs(nums[left]) > abs(nums[right]):
                arr.append(nums[left] * nums[left])
                left += 1
            else:
                arr.append(nums[right] * nums[right])
                right -= 1
        
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr

