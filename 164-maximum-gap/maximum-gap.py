class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

    # Find min and max values
        min_val = min(nums)
        max_val = max(nums)
        if min_val == max_val:
            return 0

        diff = max_val - min_val
    # Size of each bucket, at least 1
        bucket_size = max(1, diff // (n - 1))
    # Number of buckets needed
        bucket_count = diff // bucket_size + 1

    # Initialize buckets
        bucket_min = [float('inf')] * bucket_count
        bucket_max = [float('-inf')] * bucket_count

    # Distribute numbers into buckets
        for num in nums:
            idx = (num - min_val) // bucket_size
            bucket_min[idx] = min(bucket_min[idx], num)
            bucket_max[idx] = max(bucket_max[idx], num)

    # Scan buckets to compute maximum gap
        max_gap = 0
        prev_max = min_val          # smallest element
        for i in range(bucket_count):
            if bucket_min[i] == float('inf'):   # empty bucket
                continue
        # Gap between previous maximum and current minimum
            max_gap = max(max_gap, bucket_min[i] - prev_max)
            prev_max = bucket_max[i]

        return max_gap
        
