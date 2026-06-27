class Solution:
    def minFlips(self, target: str) -> int:
        ans = 0
        flipped = False

        for ch in target:
            current = '1' if flipped else '0'

            if current != ch:
                ans += 1
                flipped = not flipped

        return ans
        