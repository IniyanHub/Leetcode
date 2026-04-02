class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0

        # dp[c] will store the length of the longest substring in s 
        # that ends with the character c (where c is mapped to 0-25).
        # We only need size 26 for lowercase English letters.
        dp = [0] * 26
        
        # curr_len tracks the length of the current valid consecutive sequence ending at index i
        curr_len = 0
        
        for i in range(len(s)):
            # Check if the current character follows the previous one in the wraparound string.
            # (ord(s[i]) - ord(s[i-1])) % 26 == 1 handles both normal cases (e.g., 'b' - 'a' = 1)
            # and the wraparound case ('a' - 'z' = -25, which is 1 modulo 26).
            if i > 0 and (ord(s[i]) - ord(s[i-1])) % 26 == 1:
                curr_len += 1
            else:
                curr_len = 1
            
            # Get the index corresponding to the character (0 for 'a', 25 for 'z')
            char_index = ord(s[i]) - ord('a')
            
            # Update the maximum length found for this ending character.
            # We keep the maximum length because a longer valid substring ending in 'c'
            # implies the existence of all shorter valid suffixes ending in 'c'.
            # For example, if the longest valid substring ending in 'b' is "zab" (length 3),
            # it implies "ab" (length 2) and "b" (length 1) also exist.
            dp[char_index] = max(dp[char_index], curr_len)
        
        # The total number of unique substrings is the sum of the longest lengths
        # found for each character, as each represents a set of unique substrings
        # ending with that character.
        return sum(dp)
        