class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        seen = {0}
        prefix = 0
        ans = 0

        for num in nums:
            prefix += num

            if prefix - target in seen:
                ans += 1
                prefix = 0
                seen = {0}
            else:
                seen.add(prefix)

        return ans
        