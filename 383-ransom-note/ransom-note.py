class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_count = {}

    # Count characters in magazine
        for ch in magazine:
            char_count[ch] = char_count.get(ch, 0) + 1

    # Check ransomNote
        for ch in ransomNote:
            if char_count.get(ch, 0) == 0:
                return False
            char_count[ch] -= 1

        return True
        