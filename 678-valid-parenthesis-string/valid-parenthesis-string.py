class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0   # minimum open brackets
        high = 0  # maximum open brackets

        for ch in s:
            if ch == '(':
                low += 1
                high += 1
            elif ch == ')':
                low -= 1
                high -= 1
            else:  # '*'
                low -= 1      # treat as ')'
                high += 1     # or treat as '('

            # high < 0 means too many ')'
            if high < 0:
                return False

            # low should not go below 0
            if low < 0:
                low = 0

        return low == 0