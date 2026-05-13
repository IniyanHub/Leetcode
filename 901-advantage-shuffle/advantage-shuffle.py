class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        
        nums1.sort()
        
        # Store nums2 values with original indices
        arr = sorted((num, idx) for idx, num in enumerate(nums2))
        
        result = [0] * n
        
        left = 0
        right = n - 1
        
        # Assign numbers greedily
        for num in nums1:
            
            # If current num can beat smallest nums2
            if num > arr[left][0]:
                idx = arr[left][1]
                result[idx] = num
                left += 1
            
            # Otherwise sacrifice against largest nums2
            else:
                idx = arr[right][1]
                result[idx] = num
                right -= 1
        
        return result
        