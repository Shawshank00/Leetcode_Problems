class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        k = k % len(nums)

        temp = nums[len(nums)-k:]

        for i in range(len(nums)-1,k-1,-1):
            nums[i] = nums[i-k]
        
        for i in range(len(temp)):
            nums[i] = temp[i]
        
        print(nums)
            
