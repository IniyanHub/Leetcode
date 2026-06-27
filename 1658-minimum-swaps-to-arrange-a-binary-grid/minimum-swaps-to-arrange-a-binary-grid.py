class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Count trailing zeros in each row
        zeros = []
        for row in grid:
            count = 0
            for x in reversed(row):
                if x == 0:
                    count += 1
                else:
                    break
            zeros.append(count)

        ans = 0

        for i in range(n):
            need = n - 1 - i

            j = i
            while j < n and zeros[j] < need:
                j += 1

            if j == n:
                return -1

            while j > i:
                zeros[j], zeros[j - 1] = zeros[j - 1], zeros[j]
                ans += 1
                j -= 1

        return ans
        