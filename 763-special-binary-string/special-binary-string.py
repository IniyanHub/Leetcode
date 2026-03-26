class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if not s:
            return s
        
        # Decompose into primitive special substrings
        parts = []
        count = 0
        start = 0
        for i, ch in enumerate(s):
            count += 1 if ch == '1' else -1
            if count == 0:
                parts.append(s[start:i+1])
                start = i + 1
        
        # Recursively optimize each primitive substring
        optimized = []
        for part in parts:
            inner = part[1:-1]                 # remove the outer '1' and '0'
            opt_inner = self.makeLargestSpecial(inner)
            opt_part = '1' + opt_inner + '0'   # wrap with fixed outer chars
            optimized.append(opt_part)
        
        # The best overall order is descending lexicographic
        optimized.sort(reverse=True)
        return ''.join(optimized)
        