class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def feasible(threshold: int) -> bool:
      
            count = 1          # number of subarrays needed
            current_sum = 0
            for num in nums:
                if current_sum + num > threshold:
                    count += 1
                    current_sum = num
                    if count > k:   # already need more than k subarrays
                        return False
                else:
                    current_sum += num
            return True

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
        