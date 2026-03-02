class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return True
            
            # When we cannot decide which side is sorted due to duplicates
            if nums[left] == nums[mid] and nums[mid] == nums[right]:
                left += 1
                right -= 1
            # Left part [left, mid] is sorted
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right part [mid, right] is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False
        