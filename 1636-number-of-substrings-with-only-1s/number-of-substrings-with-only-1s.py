class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        count = 0
        result = 0

        for ch in s:
            if ch == '1':
                count += 1        # increase streak of 1's
            else:
                result = (result + count * (count + 1) // 2) % MOD
                count = 0         # reset streak
                
        # Add last streak if string ends with 1's
        result = (result + count * (count + 1) // 2) % MOD
        
        return result
        