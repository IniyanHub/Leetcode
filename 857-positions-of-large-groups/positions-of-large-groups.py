class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        n = len(s)
    
        i = 0  # start of group
    
        while i < n:
            j = i
        
        # move j until group ends
            while j < n and s[j] == s[i]:
                j += 1
        
        # group length = j - i
            if j - i >= 3:
                result.append([i, j - 1])
        
            i = j  # move to next group
    
        return result
        