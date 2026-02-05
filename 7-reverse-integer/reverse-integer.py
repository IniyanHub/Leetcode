class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if x == 0:
            return 0

    # The only 32‑bit integer whose absolute value overflows
        if x == INT_MIN:
            return 0

        sign = 1 if x > 0 else -1
        n = abs(x)
        rev = 0

        while n != 0:
            digit = n % 10
            n //= 10
        # Check for overflow before updating rev
            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and digit > INT_MAX % 10):
                return 0
            rev = rev * 10 + digit

        return sign * rev

        