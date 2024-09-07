class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        cur_sum = 0

        for i in range(k):
            cur_sum += nums[i]
        
        cur_avg = cur_sum / k

        for i in range(k,len(nums)):
            cur_sum = cur_sum + nums[i] - nums[i-k]
            cur_avg = max(cur_avg, cur_sum / k)
        return cur_avg
