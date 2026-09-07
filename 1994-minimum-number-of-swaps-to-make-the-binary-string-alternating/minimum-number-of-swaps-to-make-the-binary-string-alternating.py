class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)

        zeros = s.count('0')
        ones = n - zeros

        # If the difference is greater than 1,
        # alternating string is impossible
        if abs(zeros - ones) > 1:
            return -1

        # Count mismatches for pattern starting with 0
        mismatch0 = 0

        for i in range(n):
            expected = '0' if i % 2 == 0 else '1'

            if s[i] != expected:
                mismatch0 += 1

        # Count mismatches for pattern starting with 1
        mismatch1 = 0

        for i in range(n):
            expected = '1' if i % 2 == 0 else '0'

            if s[i] != expected:
                mismatch1 += 1

        # Choose the valid pattern
        if zeros > ones:
            # Must start with 0
            return mismatch0 // 2

        elif ones > zeros:
            # Must start with 1
            return mismatch1 // 2

        else:
            # Both patterns are possible
            return min(mismatch0, mismatch1) // 2
        