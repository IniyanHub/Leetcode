class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        n = len(start)
        if n != len(result):
            return False
    
        i = j = 0
        while i < n and j < n:
        # skip 'X' in start
            while i < n and start[i] == 'X':
                i += 1
        # skip 'X' in result
            while j < n and result[j] == 'X':
                j += 1
        
        # if both reached the end, break
            if i == n and j == n:
                break
        # if only one reached the end, the other has a non-X character left
            if i == n or j == n:
                return False
        
        # characters must match
            if start[i] != result[j]:
                return False
        
        # check movement constraints
            if start[i] == 'L' and i < j:   # L cannot move right
                return False
            if start[i] == 'R' and i > j:   # R cannot move left
                return False
        
        # move to next character
            i += 1
            j += 1
    
    # skip any trailing 'X'
        while i < n and start[i] == 'X':
            i += 1
        while j < n and result[j] == 'X':
            j += 1
    
        return i == n and j == n
        