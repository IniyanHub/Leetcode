class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
    # Otherwise, the longer string itself (or either when lengths are equal) is an uncommon subsequence.
    # Its length is the maximum possible length of any subsequence from a or b.
    
        return max(len(a), len(b))

        