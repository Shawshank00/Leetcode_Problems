
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        '''    
        #1 Solution:
        
        s_dict = Counter(s)
        t_dict = Counter(t)

        return s_dict == t_dict 
       '''
        #2 Solution:
        S = {}
        T = {}

        for i in range(len(s)):

            if s[i] in S:
                S[s[i]] += 1
            else:
                S[s[i]] = 1

            if t[i] in T:
                T[t[i]] += 1
            else:
                T[t[i]] = 1
        
        return S == T
