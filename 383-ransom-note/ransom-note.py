class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = [0] * 26
        for ch in magazine:
            counts[ord(ch) - ord('a')] += 1

    # Check ransomNote against available letters
        for ch in ransomNote:
            idx = ord(ch) - ord('a')
            if counts[idx] == 0:
                return False
            counts[idx] -= 1

        return True
        