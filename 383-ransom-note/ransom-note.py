class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counts = Counter(magazine)
    
    # Try to build the ransom note
        for ch in ransomNote:
            if magazine_counts[ch] == 0:  # Not enough of this character
                return False
            magazine_counts[ch] -= 1  # Use one occurrence
        
        return True
        