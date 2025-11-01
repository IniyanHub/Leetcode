class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        n = len(nums)

    # 1. Place each number v (1 <= v <= n) at index v-1
        for i in range(n):
        # Keep swapping until the current element is either out of range,
        # already in the right place, or a duplicate of its target.
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                target_idx = nums[i] - 1
            # swap nums[i] with nums[target_idx]
                nums[i], nums[target_idx] = nums[target_idx], nums[i]

    # 2. Find the first index where the value is not i+1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

    # 3. All positions are correct → answer is n+1
        return n + 1
        