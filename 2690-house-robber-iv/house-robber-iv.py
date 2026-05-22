class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def canRob(cap):
            count = 0
            i = 0
            
            while i < len(nums):
                if nums[i] <= cap:
                    count += 1
                    i += 2      # skip adjacent house
                else:
                    i += 1
            
            return count >= k
        
        low = min(nums)
        high = max(nums)
        
        while low < high:
            mid = (low + high) // 2
            
            if canRob(mid):
                high = mid
            else:
                low = mid + 1
        
        return low
        