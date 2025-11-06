class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i, j = 0, 0
        starIdx = -1
        iIdx = -1
    
        while i < len(s):
            if j < len(p) and (p[j] == '?' or p[j] == s[i]):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                starIdx = j
                iIdx = i
                j += 1
            elif starIdx != -1:
                j = starIdx + 1
                iIdx += 1
                i = iIdx
            else:
                return False
    
        while j < len(p) and p[j] == '*':
            j += 1
    
        return j == len(p)
        