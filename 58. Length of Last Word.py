class Solution:
    def lengthOfLastWord(self, s: str) -> int:

      #1 Solution
        a = list(s.strip().split())
        return len(a[-1])
        
      #2 Solution
        n = len(s)-1
        count = 0

        while n>=0 and s[n] == ' ':
            n = n-1
        
        while n>=0 and s[n] != ' ':
            n = n-1
            count = count + 1
        
        return count
        
