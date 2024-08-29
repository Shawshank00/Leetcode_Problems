class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        
        for i in range(len(a)//2):
            if a[i] != a[len(a)-i-1]:
                return False
        return True

