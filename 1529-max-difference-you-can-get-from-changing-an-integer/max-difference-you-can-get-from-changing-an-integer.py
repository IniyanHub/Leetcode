class Solution:
    def maxDiff(self, num: int) -> int:
        s = list(str(num))

        # ---------- Maximum ----------
        max_s = s[:]

        for ch in max_s:
            if ch != '9':
                x = ch
                max_s = ['9' if c == x else c for c in max_s]
                break

        a = int("".join(max_s))

        # ---------- Minimum ----------
        min_s = s[:]

        if min_s[0] != '1':
            x = min_s[0]
            min_s = ['1' if c == x else c for c in min_s]

        else:
            for i in range(1, len(min_s)):
                if min_s[i] not in ['0', '1']:
                    x = min_s[i]
                    min_s = ['0' if c == x else c for c in min_s]
                    break

        b = int("".join(min_s))

        return a - b
        