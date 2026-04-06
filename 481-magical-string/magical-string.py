class Solution:
    def magicalString(self, n: int) -> int:
        
        if n <= 0:
            return 0
        if n <= 3:
            return 1

        s = [1, 2, 2]
        i = 2
        num = 1

        while len(s) < n:
            count = s[i]
            for _ in range(count):
                s.append(num)
            num = 2 if num == 1 else 1
            i += 1

        return s[:n].count(1)
        