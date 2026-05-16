class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        freq = {}

        # Count words from first sentence
        for word in s1.split():
            freq[word] = freq.get(word, 0) + 1

        # Count words from second sentence
        for word in s2.split():
            freq[word] = freq.get(word, 0) + 1

        # Collect uncommon words
        result = []

        for word in freq:
            if freq[word] == 1:
                result.append(word)

        return result
        