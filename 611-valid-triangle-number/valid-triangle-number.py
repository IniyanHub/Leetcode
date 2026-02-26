class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        n = len(nums)
    
    # Iterate from the end, treating nums[k] as the largest side
        for k in range(n - 1, 1, -1):
            left = 0
            right = k - 1
        
            while left < right:
                if nums[left] + nums[right] > nums[k]:
                # KEY STEP: We add all pairs between left and right
                # If this line is count += 1, you will get the wrong answer (2)
                    count += right - left
                    right -= 1
                else:
                    left += 1
                
        return count
        