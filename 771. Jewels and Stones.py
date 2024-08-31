class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        count = 0

        for i in stones:
            if i in h:
                count += 1
        return count
