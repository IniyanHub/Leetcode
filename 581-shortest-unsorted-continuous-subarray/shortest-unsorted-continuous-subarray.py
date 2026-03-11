class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

    # Find the rightmost index that needs to be sorted
        max_from_left = nums[0]
        right = -1
        for i in range(1, n):
            max_from_left = max(max_from_left, nums[i])
            if nums[i] < max_from_left:
                right = i

    # If no such index, the array is already sorted
        if right == -1:
            return 0

    # Find the leftmost index that needs to be sorted
        min_from_right = nums[-1]
        left = n
        for i in range(n - 2, -1, -1):
            min_from_right = min(min_from_right, nums[i])
            if nums[i] > min_from_right:
                left = i

        return right - left + 1
        