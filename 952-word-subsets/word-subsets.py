class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        required = Counter()

        # Build combined requirement from words2
        for word in words2:
            freq = Counter(word)
            for ch in freq:
                required[ch] = max(required[ch], freq[ch])

        result = []

        # Check each word in words1
        for word in words1:
            freq = Counter(word)

            valid = True

            for ch in required:
                if freq[ch] < required[ch]:
                    valid = False
                    break

            if valid:
                result.append(word)

        return result
        