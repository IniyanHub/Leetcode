class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1   # smallest number we cannot form
        i = 0
        patches = 0
    
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
            # patch with 'miss'
                miss += miss
                patches += 1
    
        return patches

        