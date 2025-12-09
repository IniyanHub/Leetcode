class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        reversed_num = 0
        # Define the 32-bit signed integer limits.
        INT_MAX = 2**31 - 1  # 2147483647

        while x != 0:
            # Get the last digit of x.
            digit = x % 10

            # Check for overflow before appending the digit.
            # If reversed_num is already larger than INT_MAX // 10,
            # then reversed_num * 10 will definitely overflow.
            # If reversed_num is equal to INT_MAX // 10, then the
            # new digit must be less than or equal to INT_MAX % 10.
            if reversed_num > INT_MAX // 10 or (reversed_num == INT_MAX // 10 and digit > INT_MAX % 10):
                return 0

            # Append the digit to the reversed number.
            reversed_num = reversed_num * 10 + digit

            # Remove the last digit from x.
            x //= 10

        return sign * reversed_num

        