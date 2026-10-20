class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        count = Counter(words)
        length = 0
        center = False

        for word in count:
            reverse = word[::-1]

            if word == reverse:
                # Words like "gg", "cc", "ll"
                pairs = count[word] // 2
                length += pairs * 4

                if count[word] % 2 == 1:
                    center = True
            elif word < reverse:
                # Pair words like "lc" and "cl"
                pairs = min(count[word], count[reverse])
                length += pairs * 4

        if center:
            length += 2

        return length
        