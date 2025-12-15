class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
    
    # Step 1: Find the rightmost index i where nums[i] < nums[i+1]
        i = n - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
    
    # Step 2: If such an index exists
        if i >= 0:
        # Step 3: Find the rightmost index j where nums[j] > nums[i]
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
        
        # Step 4: Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]
    
    # Step 5: Reverse the subarray nums[i+1:]
        left, right = i+1, n-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        