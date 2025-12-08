class Solution:
    def convertToBase7(self, num: int) -> str:
        # Special case for zero
        if num == 0:
            return "0"

    # Remember the sign and work with absolute value
        sign = '-' if num < 0 else ''
        x = abs(num)

        digits = []
        while x > 0:
            digit = x % 7
            digits.append(str(digit))   # store as character
            x //= 7

    # Digits are collected least‑significant first → reverse them
        base7 = ''.join(reversed(digits))

        return sign + base7
        