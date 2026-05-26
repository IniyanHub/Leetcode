class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        stack = []

        letter_count = s.count(letter)
        need = repetition

        for i, ch in enumerate(s):

            # Remove bigger chars if possible
            while stack and stack[-1] > ch:

                # Remaining characters after pop
                remaining = len(s) - i - 1

                # Can we still build size k?
                if len(stack) - 1 + remaining + 1 < k:
                    break

                # If popping required letter
                if stack[-1] == letter:
                    if letter_count <= need:
                        break
                    need += 1

                stack.pop()

            # Add current character if size < k
            if len(stack) < k:

                if ch == letter:
                    stack.append(ch)
                    need -= 1

                else:
                    # Reserve space for required letters
                    if k - len(stack) > need:
                        stack.append(ch)

            # Update remaining letter count
            if ch == letter:
                letter_count -= 1

        return "".join(stack)
        