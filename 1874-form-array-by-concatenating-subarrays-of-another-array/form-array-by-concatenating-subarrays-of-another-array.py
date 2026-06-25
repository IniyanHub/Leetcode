class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        pos = 0
        n = len(nums)

        for group in groups:
            m = len(group)
            found = False

            while pos + m <= n:
                if nums[pos:pos + m] == group:
                    pos += m  # move past the matched subarray
                    found = True
                    break
                pos += 1

            if not found:
                return False

        return True
        