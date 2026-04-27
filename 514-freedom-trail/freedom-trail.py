class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
    
    # Store all positions of each character
        pos_map = defaultdict(list)
        for i, ch in enumerate(ring):
            pos_map[ch].append(i)
    
        @lru_cache(None)
        def dp(pos, k):
        # If all characters are processed
            if k == len(key):
                return 0
        
            res = float('inf')
        
        # Try all positions of current character
            for target in pos_map[key[k]]:
                diff = abs(pos - target)
                step = min(diff, n - diff)  # circular distance
            
            # +1 for pressing button
                res = min(res, step + 1 + dp(target, k + 1))
        
            return res
    
        return dp(0, 0)
        