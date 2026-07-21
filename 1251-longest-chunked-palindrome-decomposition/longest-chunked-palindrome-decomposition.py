class Solution:
    def longestDecomposition(self, text: str) -> int:
        def solve(s):
            n = len(s)

            for i in range(1, n // 2 + 1):
                if s[:i] == s[n - i:]:
                    return 2 + solve(s[i:n - i])

            return 1 if s else 0

        return solve(text)
        