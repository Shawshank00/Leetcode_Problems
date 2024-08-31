class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        J = set(jewels)
        
        count = 0

        for i in stones:
            if i in J:
                count += 1
        return count
