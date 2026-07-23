class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last = {}

        # Store the last occurrence of each digit
        for i, d in enumerate(digits):
            last[int(d)] = i

        # Try to swap with the largest possible digit
        for i, d in enumerate(digits):
            curr = int(d)
            for bigger in range(9, curr, -1):
                if bigger in last and last[bigger] > i:
                    digits[i], digits[last[bigger]] = digits[last[bigger]], digits[i]
                    return int("".join(digits))

        return num
        