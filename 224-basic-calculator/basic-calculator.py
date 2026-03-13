class Solution:
    def calculate(self, s: str) -> int:
        result = 0          # accumulated result so far
        num = 0             # current number being built
        sign = 1            # sign for the current number (1 = +, -1 = -)
        stack = []          # stack for (result, sign) when entering '('
        last_char = None    # last non-space character type

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
                last_char = 'digit'
            elif ch == '+' or ch == '-':
            # Determine if this operator is unary or binary
                if last_char is None or last_char == '(' or last_char in '+-':
                # Unary operator
                    if ch == '-':
                        sign = -sign
                # Unary '+' does nothing
                else:
                # Binary operator
                    result += sign * num
                    num = 0
                    sign = 1 if ch == '+' else -1
                last_char = ch
            elif ch == '(':
            # Save current context and start a new one
                stack.append((result, sign))
                result = 0
                sign = 1
                last_char = '('
            elif ch == ')':
            # Finish the current number and combine with the context before '('
                result += sign * num
                num = 0
                prev_result, prev_sign = stack.pop()
                result = prev_result + prev_sign * result
                last_char = ')'
        result += sign * num
        return result