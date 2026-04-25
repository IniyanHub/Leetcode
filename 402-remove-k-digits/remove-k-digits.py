class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
        # Remove larger digits from stack
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

    # If k still left, remove from end
        while k > 0:
            stack.pop()
            k -= 1

    # Build result and remove leading zeros
        result = ''.join(stack).lstrip('0')

        return result if result else "0"
        