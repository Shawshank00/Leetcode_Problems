class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        n = len(cardPoints)
        cur_sum = sum(cardPoints[:k])   #sum of 1st k integers
        max_sum = cur_sum               #Lets assume this is the max_sum for now


        #lets eliminate 1 by one and add from end of list and track max sum
      
        for i in range(1,k+1):
            cur_sum = cur_sum - cardPoints[k-i] + cardPoints[n-i]
            max_sum = max(max_sum, cur_sum)
        return max_sum

        #O(n) & O(1)
