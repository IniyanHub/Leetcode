class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0

        # Calculate length of decoded string
        for ch in s:
            if ch.isdigit():
                size *= int(ch)
            else:
                size += 1

        # Traverse backwards
        for ch in reversed(s):

            k %= size

            # If current character is answer
            if k == 0 and ch.isalpha():
                return ch

            # Reduce size
            if ch.isdigit():
                size //= int(ch)
            else:
                size -= 1
        