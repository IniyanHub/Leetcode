class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        original = n
        place = 1

        while sum(map(int, str(n))) > target:
            digit = (n // place) % 10

            if digit != 0:
                n = n + (10 - digit) * place

            place *= 10

        return n - original
        