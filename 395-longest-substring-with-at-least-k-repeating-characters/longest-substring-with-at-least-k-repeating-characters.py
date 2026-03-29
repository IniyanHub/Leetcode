class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k <= 0:
            return len(s)

        n = len(s)
        max_len = 0

    # The string contains only lowercase English letters, so at most 26 unique characters.
        for u in range(1, 27):               # u = maximum number of unique characters allowed in the window
            freq = [0] * 26                  # frequency of each character in the current window
            left = 0
            num_unique = 0                   # number of distinct characters in the window
            num_at_least_k = 0               # number of distinct characters with count >= k

            for right in range(n):
                idx_r = ord(s[right]) - ord('a')

            # Add the new character to the window
                if freq[idx_r] == 0:
                    num_unique += 1
                freq[idx_r] += 1
                if freq[idx_r] == k:
                    num_at_least_k += 1

            # Shrink the window until it has at most u unique characters
                while num_unique > u:
                    idx_l = ord(s[left]) - ord('a')
                    if freq[idx_l] == k:
                        num_at_least_k -= 1
                    freq[idx_l] -= 1
                    if freq[idx_l] == 0:
                        num_unique -= 1
                    left += 1

            # If every character in the window appears at least k times, update the answer
                if num_unique == num_at_least_k:
                    max_len = max(max_len, right - left + 1)

        return max_len
        