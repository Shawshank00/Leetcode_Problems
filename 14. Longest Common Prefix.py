#1:
class Solution:
    def longestCommonPrefix(self, strs):
        min_length = float('inf')
        for s in strs:
            if len(s) < min_length:
                min_length = len(s)
        
        i = 0
        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i += 1
        
        return strs[0][:i]


#2:
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        v = sorted(strs)
        a = v[0]
        b = v[-1]

        for i in range(min(len(a),len(b))):
            if a[i] != b[i]:
                return ans
            else:
                ans = ans + a[i]
        return ans

#3:
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefix = strs[0]
        for string in strs[1:]:
            while string.find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
