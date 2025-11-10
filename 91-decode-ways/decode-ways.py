class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)

        # prev2 corresponds to dp[i-2], prev1 corresponds to dp[i-1]
        # dp[i] is the number of ways to decode the first i characters of s.
        
        # dp[0] = 1 (one way to decode an empty string)
        prev2 = 1
        
        # dp[1] = 1 if the first character is not '0', 0 otherwise.
        # The initial check for s[0] == '0' handles this, so prev1 is 1.
        prev1 = 1

        # Iterate from the third character (i=2) to the end of the string.
        for i in range(2, n + 1):
            current = 0
            
            # Check for a valid single-digit decode (the i-th character, s[i-1]).
            # A '0' cannot be decoded alone.
            if s[i-1] != '0':
                current += prev1
            
            # Check for a valid two-digit decode (s[i-2:i]).
            # The number must be between 10 and 26, inclusive.
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                current += prev2
            
            # Update the previous values for the next iteration.
            prev2 = prev1
            prev1 = current
            
        return prev1

        