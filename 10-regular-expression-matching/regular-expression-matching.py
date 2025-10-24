class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # dp[i][j] will be True if the first i characters of s match the first j characters of p.
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: empty string matches empty pattern.
        dp[0][0] = True
        
        # Base case: empty string s vs. non-empty pattern p.
        # This is only possible if p can represent an empty string, e.g., a*, a*b*, etc.
        for j in range(1, n + 1):
            # If the current pattern character is '*', it can match zero occurrences
            # of the preceding element. So, we look two positions back in the pattern.
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # Fill the DP table for non-empty strings.
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Case 1: The pattern character is a '.' or matches the string character directly.
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    # The result depends on the match of the previous substrings.
                    dp[i][j] = dp[i - 1][j - 1]
                
                # Case 2: The pattern character is '*'.
                elif p[j - 1] == '*':
                    # Sub-case 2.1: '*' matches zero occurrences of the preceding element (p[j-2]).
                    # We check if the string matches the pattern up to j-2.
                    dp[i][j] = dp[i][j - 2]
                    
                    # Sub-case 2.2: '*' matches one or more occurrences of the preceding element.
                    # This is possible if the preceding element (p[j-2]) matches the current string character (s[i-1]).
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        # If it matches, we check if the rest of the string (s[:i-1])
                        # matches the same pattern (p[:j]).
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                
                # Case 3: Characters do not match.
                else:
                    dp[i][j] = False
        
        # The final result is whether the entire string matches the entire pattern.
        return dp[m][n]