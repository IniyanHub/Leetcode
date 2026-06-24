class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        choose = len(slices) // 3

        def solve(nums):
            m = len(nums)

            dp = [[0] * (choose + 1) for _ in range(m + 1)]

            for i in range(1, m + 1):
                for j in range(1, min((i + 1) // 2, choose) + 1):
                    dp[i][j] = max(
                        dp[i - 1][j],
                        (dp[i - 2][j - 1] if i >= 2 else 0) + nums[i - 1]
                    )

            return dp[m][choose]

        return max(
            solve(slices[:-1]),  # exclude last
            solve(slices[1:])    # exclude first
        )
        