class Solution:
    def nextGreaterElement(self, n: int) -> int:
        MAX_INT = 2**31 - 1
    
    # Early exit: if n already exceeds 32-bit max, no valid answer can fit.
        if n > MAX_INT:
            return -1

    # Convert n to a mutable list of digit characters.
        digits = list(str(n))

    # Step 1: find the first decreasing digit from the right.
        i = len(digits) - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
        if i == -1:
            return -1  # digits are in non-increasing order.

    # Step 2: find the smallest digit larger than digits[i] to its right.
        j = len(digits) - 1
        while j > i and digits[j] <= digits[i]:
            j -= 1

    # Step 3: swap them.
        digits[i], digits[j] = digits[j], digits[i]

    # Step 4: reverse the suffix (i+1 to end) to make it ascending.
        left, right = i + 1, len(digits) - 1
        while left < right:
            digits[left], digits[right] = digits[right], digits[left]
            left += 1
            right -= 1

    # Convert back to integer.
        result = int(''.join(digits))

    # Step 5: check 32-bit integer range.
        return result if result <= MAX_INT else -1
        