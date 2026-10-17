class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 10**9 + 7

        max_num = (1 << p) - 1
        exponent = (1 << (p - 1)) - 1

        return (max_num * pow(max_num - 1, exponent, MOD)) % MOD
        