class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        while x != 0:
            # Python's // is floor division. To mimic C++/Java's truncation
            # towards zero, we use int(x / 10).
            # Python's % operator gives a positive remainder for negative numbers.
            # To get the correct negative digit, we use x % -10.
            pop = x % 10 if x >= 0 else x % -10
            x = int(x / 10)

            # --- Overflow Check ---
            # Before multiplying rev by 10, check if it would cause an overflow.
            # The environment is assumed to be 32-bit, so we must simulate this.
            
            # Check for positive overflow
            if rev > INT_MAX / 10 or (rev == INT_MAX / 10 and pop > 7):
                return 0
            
            # Check for negative overflow
            if rev < INT_MIN / 10 or (rev == INT_MIN / 10 and pop < -8):
                return 0
            
            # Append the digit to the reversed number
            rev = rev * 10 + pop
            
        return rev
        
        