class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = 0
        yx = 0
    
        for a, b in zip(s1, s2):
            if a == b:
                continue
            elif a == 'x' and b == 'y':
                xy += 1
            elif a == 'y' and b == 'x':
                yx += 1
    
    # If odd mismatches → impossible
        if (xy + yx) % 2 != 0:
            return -1
    
    # Calculate swaps
        return (xy // 2) + (yx // 2) + (2 if xy % 2 else 0)
        