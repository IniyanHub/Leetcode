class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        
        # Frequency counts for digits that are not bulls
        # Counts for digits in secret (not matched positionally)
        s_counts = [0] * 10
        # Counts for digits in guess (not matched positionally)
        g_counts = [0] * 10
        
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                # Increment the count for the respective digits
                s_counts[int(s)] += 1
                g_counts[int(g)] += 1
        
        # Calculate cows by summing the minimum counts for each digit
        for i in range(10):
            cows += min(s_counts[i], g_counts[i])
            
        return f"{bulls}A{cows}B"