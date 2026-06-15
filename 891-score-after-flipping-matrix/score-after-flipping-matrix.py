class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        score = 0

        for j in range(n):
            ones = 0

            for i in range(m):
                # If row would be flipped (first bit is 0),
                # the value at grid[i][j] becomes 1 - grid[i][j]
                if grid[i][0] == 1:
                    ones += grid[i][j]
                else:
                    ones += 1 - grid[i][j]

            ones = max(ones, m - ones)

            score += ones * (1 << (n - 1 - j))

        return score
        