class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, L = len(s1), len(s2), len(s3)
        if n + m != L:
            return False

    # Use a 1‑D DP array of size (m+1) – iterate over i (s1) rows.
        dp = [False] * (m + 1)
        dp[0] = True  # empty prefixes

    # First row (i == 0): only characters from s2 are used.
        for j in range(1, m + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

    # Process rows i = 1 .. n
        for i in range(1, n + 1):
        # Update dp[0] for the current i (only s1 contributes)
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]

            for j in range(1, m + 1):
            # position in s3 is i + j - 1
                from_s1 = dp[j] and s1[i - 1] == s3[i + j - 1]
                from_s2 = dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                dp[j] = from_s1 or from_s2

        return dp[m]