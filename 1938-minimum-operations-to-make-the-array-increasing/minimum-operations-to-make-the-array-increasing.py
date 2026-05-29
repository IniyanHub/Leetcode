class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0

        for i in range(1, len(nums)):

            # If current element is not greater
            if nums[i] <= nums[i - 1]:

                # Needed value
                needed = nums[i - 1] + 1

                # Count operations
                operations += needed - nums[i]

                # Update array
                nums[i] = needed

        return operations
        
        