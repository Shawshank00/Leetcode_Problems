class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}
        n = len(nums) // 3

        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        return [a for a,b in hashmap.items() if b > n]


        #Time Complexity:O(n) where n is the number of elements in nums, due to single traversal of nums and hashmap items
        #Space Complexity:O(n) for storing elements in the hashmap in the worst case
