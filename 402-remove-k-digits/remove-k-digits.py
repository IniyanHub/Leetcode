class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
    
        for digit in num:
        # While we still need to remove digits (k > 0), the stack is not empty,
        # and the top of the stack is greater than the current digit,
        # we pop the stack to make the number smaller.
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
    
    # If we haven't removed enough digits (e.g., num is strictly increasing like "12345"),
    # remove the remaining k digits from the end of the stack.
        if k > 0:
            stack = stack[:-k]
    
    # Convert the stack to a string and remove leading zeros.
    # If the result is an empty string, return "0".
        result = "".join(stack).lstrip("0")
    
        return result if result else "0"
        