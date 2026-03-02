class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        current_sum = 0
        min_length = float('inf')
        
        for right in range(n):
            # Expand the window by including the element at the right pointer
            current_sum += nums[right]
            
            # While the current sum meets the target, try to shrink the window
            while current_sum >= target:
                # Update the minimum length found so far
                min_length = min(min_length, right - left + 1)
                
                # Shrink the window from the left
                current_sum -= nums[left]
                left += 1
                
        # Return 0 if no valid subarray found, otherwise return min_length
        return 0 if min_length == float('inf') else min_length
        