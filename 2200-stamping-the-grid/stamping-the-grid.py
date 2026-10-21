class Solution:
    def possibleToStamp(self, grid: list[list[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])

        # Step 1: Build prefix sum of occupied cells
        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = (
                    grid[i][j]
                    + prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                )

        # Step 2: Difference array for stamp coverage
        diff = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - stampHeight + 1):
            for j in range(n - stampWidth + 1):

                # Count occupied cells in this stamp rectangle
                occupied = (
                    prefix[i + stampHeight][j + stampWidth]
                    - prefix[i][j + stampWidth]
                    - prefix[i + stampHeight][j]
                    + prefix[i][j]
                )

                # Place a stamp only if the entire area is empty
                if occupied == 0:
                    diff[i][j] += 1
                    diff[i + stampHeight][j] -= 1
                    diff[i][j + stampWidth] -= 1
                    diff[i + stampHeight][j + stampWidth] += 1

        # Step 3: Calculate coverage and check empty cells
        for i in range(m):
            for j in range(n):
                if i > 0:
                    diff[i][j] += diff[i - 1][j]
                if j > 0:
                    diff[i][j] += diff[i][j - 1]
                if i > 0 and j > 0:
                    diff[i][j] -= diff[i - 1][j - 1]

                if grid[i][j] == 0 and diff[i][j] == 0:
                    return False

        return True
        