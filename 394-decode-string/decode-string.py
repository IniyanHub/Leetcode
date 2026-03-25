class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        current_num = 0
        
        for char in s:
            if char.isdigit():
                # Build the multi-digit number
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push the current context to the stack
                stack.append((current_string, current_num))
                # Reset for the new inner scope
                current_string = ""
                current_num = 0
            elif char == ']':
                # Pop the context: string before the bracket and the repeat count
                prev_string, repeat_count = stack.pop()
                # Decode the current segment and append to the previous string
                current_string = prev_string + (current_string * repeat_count)
            else:
                # Append letters to the current string
                current_string += char
                
        return current_string
        