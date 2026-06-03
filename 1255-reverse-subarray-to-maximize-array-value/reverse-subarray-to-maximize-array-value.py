class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        n = len(nums)

        total = 0
        for i in range(n - 1):
            total += abs(nums[i] - nums[i + 1])

        ans = total

        # Reverse prefix or suffix
        for i in range(n - 1):
            ans = max(
                ans,
                total + abs(nums[0] - nums[i + 1]) - abs(nums[i] - nums[i + 1])
            )

            ans = max(
                ans,
                total + abs(nums[-1] - nums[i]) - abs(nums[i] - nums[i + 1])
            )

        # Reverse middle subarray
        mx = -float('inf')
        mn = float('inf')

        for i in range(n - 1):
            a, b = nums[i], nums[i + 1]
            mx = max(mx, min(a, b))
            mn = min(mn, max(a, b))

        ans = max(ans, total + 2 * (mx - mn))

        return ans
        