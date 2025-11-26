class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True                     # empty prefix is always good

    # Optional optimization: collect distinct word lengths
        word_lengths = {len(w) for w in word_set}

        for i in range(1, n + 1):
        # Only consider j that produce a suffix length present in the dictionary
            for length in word_lengths:
                j = i - length
                if j < 0:
                    continue
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break   # no need to try other j's

        return dp[n]
        