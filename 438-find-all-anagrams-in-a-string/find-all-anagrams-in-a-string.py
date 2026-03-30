class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

    # Frequency arrays for p and the sliding window in s.
        p_count = [0] * 26
        w_count = [0] * 26

    # Build frequency of p.
        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

    # Initialize the first window of length len(p).
        for i in range(len(p)):
            w_count[ord(s[i]) - ord('a')] += 1

    # Count how many character frequencies match between p and the first window.
        matches = sum(1 for i in range(26) if w_count[i] == p_count[i])

        result = []
        if matches == 26:
            result.append(0)

    # Slide the window over the rest of s.
        for i in range(len(p), len(s)):
        # Character that leaves the window.
            out_idx = ord(s[i - len(p)]) - ord('a')
            if w_count[out_idx] == p_count[out_idx]:
                matches -= 1
            w_count[out_idx] -= 1
            if w_count[out_idx] == p_count[out_idx]:
                matches += 1

        # Character that enters the window.
            in_idx = ord(s[i]) - ord('a')
            if w_count[in_idx] == p_count[in_idx]:
                matches -= 1
            w_count[in_idx] += 1
            if w_count[in_idx] == p_count[in_idx]:
                matches += 1

        # If all 26 frequencies match, we found an anagram.
            if matches == 26:
                result.append(i - len(p) + 1)

        return result

        