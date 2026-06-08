class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count = Counter(barcodes)

        arr = sorted(count.items(), key=lambda x: -x[1])

        n = len(barcodes)
        ans = [0] * n

        idx = 0

        for num, freq in arr:
            for _ in range(freq):
                ans[idx] = num
                idx += 2

                if idx >= n:
                    idx = 1

        return ans
        