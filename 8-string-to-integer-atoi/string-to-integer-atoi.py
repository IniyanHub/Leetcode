class Solution:
    def myAtoi(self, s: str) -> int:

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Initialize variables
        i = 0
        n = len(s)
        sign = 1
        result = 0

        # 1. Discard leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # 2. Determine the sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # 3. Convert digits to integer
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # 4. Check for overflow before updating the result
            # If result * 10 + digit > INT_MAX, it's an overflow.
            # We check this as result > (INT_MAX - digit) // 10 to avoid overflow in the multiplication.
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            # Update the result
            result = result * 10 + digit
            i += 1

        # 5. Apply the sign and return the final result
        return sign * result
        