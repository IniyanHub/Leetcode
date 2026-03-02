class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[mid + 1]:
                # We are on the descending slope, so the peak is to the left (including mid)
                right = mid
            else:
                # We are on the ascending slope, so the peak is to the right
                left = mid + 1
                
        return left
        