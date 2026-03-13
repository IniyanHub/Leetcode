class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        factor = 1
        
        while factor <= n:
            # Determine the parts of the number
            lower = n % factor
            curr = (n // factor) % 10
            higher = n // (factor * 10)
            
            if curr == 0:
                # If current digit is 0, the count depends only on the higher part
                count += higher * factor
            elif curr == 1:
                # If current digit is 1, add higher part cycles plus the current lower part
                count += higher * factor + lower + 1
            else:
                # If current digit > 1, add (higher + 1) full cycles
                count += (higher + 1) * factor
            
            factor *= 10
            
        return count
        