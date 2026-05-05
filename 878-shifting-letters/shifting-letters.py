class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        total_shift = 0
        result = list(s)
        
        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            total_shift = (total_shift + shifts[i]) % 26
            
            # Shift character
            new_char = (ord(s[i]) - ord('a') + total_shift) % 26
            result[i] = chr(new_char + ord('a'))
        
        return "".join(result)
        