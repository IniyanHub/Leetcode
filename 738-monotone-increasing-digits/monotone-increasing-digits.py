class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(str(n))
        mark = len(digits)

    # Traverse from right to left
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] < digits[i - 1]:
                digits[i - 1] = str(int(digits[i - 1]) - 1)
                mark = i

    # Fill all positions after 'mark' with '9'
        for i in range(mark, len(digits)):
            digits[i] = '9'

        return int("".join(digits))
        