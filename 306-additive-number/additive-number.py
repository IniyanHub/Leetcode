class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def is_valid(i, j):
            num1 = num[:i]
            num2 = num[i:j]

        # leading zero check
            if (num1.startswith('0') and len(num1) > 1) or \
            (num2.startswith('0') and len(num2) > 1):
                return False

            x1, x2 = int(num1), int(num2)
            k = j

            while k < n:
                x3 = x1 + x2
                x3_str = str(x3)

                if not num.startswith(x3_str, k):
                    return False

                k += len(x3_str)
                x1, x2 = x2, x3

            return True

        for i in range(1, n):
            for j in range(i + 1, n):
                if is_valid(i, j):
                    return True

        return False
        