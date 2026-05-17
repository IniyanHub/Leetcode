class Solution:
    def maxValue(self, n: str, x: int) -> str:
        x = str(x)

        # If number is negative
        if n[0] == '-':
            # Insert before first digit greater than x
            for i in range(1, len(n)):
                if n[i] > x:
                    return n[:i] + x + n[i:]

            return n + x

        # If number is positive
        else:
            # Insert before first digit smaller than x
            for i in range(len(n)):
                if n[i] < x:
                    return n[:i] + x + n[i:]

            return n + x
        