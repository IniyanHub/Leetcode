class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = ['a'] * n
        extra = k - n

        i = n - 1
        while extra > 0:
            add = min(25, extra)
            ans[i] = chr(ord('a') + add)
            extra -= add
            i -= 1

        return "".join(ans)
        