from typing import List
from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # Count required letters from licensePlate
        need = Counter(c.lower() for c in licensePlate if c.isalpha())
        
        result = ""
        
        for word in words:
            count = Counter(word)
            
            # Check if word satisfies all required letters
            if all(count[c] >= need[c] for c in need):
                if result == "" or len(word) < len(result):
                    result = word
        
        return result