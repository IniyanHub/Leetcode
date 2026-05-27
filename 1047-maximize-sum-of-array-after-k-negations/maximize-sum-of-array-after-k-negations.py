class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()

        # Convert negatives to positives
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1

        # Sort again to get smallest element
        nums.sort()

        # If k is still odd, flip smallest number
        if k % 2 == 1:
            nums[0] = -nums[0]

        return sum(nums)

        