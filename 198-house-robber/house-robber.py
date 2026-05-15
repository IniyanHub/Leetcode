class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # Base case
        if n == 1:
            return nums[0]

        # DP array
        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # Fill DP array
        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[n - 1]
        