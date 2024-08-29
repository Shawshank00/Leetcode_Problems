class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        p = 0             # track_profit
        b = float('inf')  # initial_buying_price = infinity

        for i in range(len(prices)):
            if prices[i] < b:
                b = prices[i]
            
            p = max(p, prices[i] - b)
        return p
