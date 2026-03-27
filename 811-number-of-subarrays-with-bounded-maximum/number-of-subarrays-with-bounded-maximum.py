class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ans = 0
        last_bad = -1
        last_good = -1
        
        for i, num in enumerate(nums):
            # If the number is greater than right, it invalidates subarrays containing it
            if num > right:
                last_bad = i
            
            # If the number is within the range [left, infinity), 
            # it can serve as the maximum for subarrays ending at i
            if num >= left:
                last_good = i
            
            # If we have found a valid 'max' element more recently than a 'bad' element,
            # we can form valid subarrays ending at i.
            # The start index can be anywhere from (last_bad + 1) to last_good.
            if last_good > last_bad:
                ans += last_good - last_bad
                
        return ans
        