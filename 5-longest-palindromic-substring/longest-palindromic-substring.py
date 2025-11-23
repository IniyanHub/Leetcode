class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        start = 0  # start index of the best palindrome
        max_len = 1  # its length (at least one character)

        for i in range(n):
            # ---- odd length palindrome, centre at i ----
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                cur_len = r - l + 1
                if cur_len > max_len:
                    start = l
                    max_len = cur_len
                l -= 1
                r += 1

            # ---- even length palindrome, centre between i and i+1 ----
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                cur_len = r - l + 1
                if cur_len > max_len:
                    start = l
                    max_len = cur_len
                l -= 1
                r += 1

        return s[start : start + max_len]
