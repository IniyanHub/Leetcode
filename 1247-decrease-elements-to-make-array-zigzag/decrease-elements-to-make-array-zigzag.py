class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)

        def moves(start):
            ans = 0
            for i in range(start, n, 2):
                left = nums[i - 1] if i > 0 else float('inf')
                right = nums[i + 1] if i < n - 1 else float('inf')

                target = min(left, right)

                if nums[i] >= target:
                    ans += nums[i] - target + 1

            return ans

        return min(moves(0), moves(1))
        