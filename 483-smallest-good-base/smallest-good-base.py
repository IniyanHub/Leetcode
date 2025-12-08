class Solution:
    def smallestGoodBase(self, n: str) -> str:
        N = int(n)

    # maximal possible length of all‑1 representation: 2^m - 1 <= N
        max_m = (N + 1).bit_length() - 1   # floor(log2(N+1))

    # helper: compute 1 + k + k^2 + ... + k^{m-1}, stop early if > N
        def geometric_sum(k: int, m: int, limit: int) -> int:
            total = 1
            cur = 1
            for _ in range(1, m):
                cur *= k
                total += cur
                if total > limit:
                    break
            return total

    # try lengths from largest to smallest (except m = 2, handled later)
        for m in range(max_m, 2, -1):
            low = 2
        # k^{m-1} <= N  →  k <= floor(N^{1/(m-1)})
            high = int(N ** (1.0 / (m - 1))) + 1

            while low <= high:
                k = (low + high) // 2
                s = geometric_sum(k, m, N)

                if s == N:
                    return str(k)
                if s < N:
                    low = k + 1
                else:
                    high = k - 1

    # No representation with m >= 3 → the only one is "11"
        return str(N - 1)
        