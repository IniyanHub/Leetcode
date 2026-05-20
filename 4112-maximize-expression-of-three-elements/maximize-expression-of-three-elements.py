class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        n = len(nums)

        # Largest and second largest numbers
        max1 = max2 = float('-inf')

        # Smallest number
        min_val = float('inf')

        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num

            min_val = min(min_val, num)

        return max1 + max2 - min_val
        