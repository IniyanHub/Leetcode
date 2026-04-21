class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1:-1]  # remove parentheses

        def generate(num):
            res = []

        # case 1: no decimal
            if num == "0" or not (num.startswith("0") and len(num) > 1):
                res.append(num)

        # case 2: with decimal
            for i in range(1, len(num)):
                left = num[:i]
                right = num[i:]

            # valid left: no leading zero unless single digit
                if (left.startswith("0") and len(left) > 1):
                    continue

            # valid right: no trailing zero
                if right.endswith("0"):
                    continue

                res.append(left + "." + right)

            return res

        result = []

    # split into two parts
        for i in range(1, len(s)):
            left_part = s[:i]
            right_part = s[i:]

            left_options = generate(left_part)
            right_options = generate(right_part)

            for l in left_options:
                for r in right_options:
                    result.append(f"({l}, {r})")

        return result
        