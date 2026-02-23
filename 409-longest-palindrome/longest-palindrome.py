from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        length = 0
        odd_exists = False

        for count in freq.values():
            length += (count // 2) * 2   # add even pairs
            if count % 2 == 1:
                odd_exists = True

        if odd_exists:
            length += 1   # one odd character can be the center

        return length
        