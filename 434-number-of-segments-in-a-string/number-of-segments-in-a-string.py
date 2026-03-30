class Solution:
    def countSegments(self, s: str) -> int:
        segment_count = 0
    
        for i in range(len(s)):
        # We detect the start of a new segment if the current character is not a space
        # and either it's the first character or the previous character was a space.
            if s[i] != ' ' and (i == 0 or s[i-1] == ' '):
                segment_count += 1
            
        return segment_count
        