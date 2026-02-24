class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = '+'          # the operator before the current number
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch in '+-*/':
                # apply the previous operator to the just completed number
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    # truncate toward zero
                    stack.append(int(stack.pop() / num))
                # remember the new operator and reset the number
                sign = ch
                num = 0
        # process the last number
        if sign == '+':
            stack.append(num)
        elif sign == '-':
            stack.append(-num)
        elif sign == '*':
            stack.append(stack.pop() * num)
        elif sign == '/':
            stack.append(int(stack.pop() / num))

        return sum(stack)

        