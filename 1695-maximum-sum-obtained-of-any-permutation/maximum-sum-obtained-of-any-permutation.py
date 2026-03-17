class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Initialize difference array with size n + 1 to handle boundary easily
        freq = [0] * (n + 1)
        
        # Process requests to build the difference array
        for start, end in requests:
            freq[start] += 1
            freq[end + 1] -= 1
            
        # Compute prefix sum to get the actual frequency of each index
        # The last element freq[n] is auxiliary and not used
        for i in range(1, n):
            freq[i] += freq[i - 1]
            
        # Sort both nums and frequencies in descending order
        nums.sort(reverse=True)
        freq.sort(reverse=True)
        
        # Calculate the maximum sum
        total_sum = 0
        for i in range(n):
            total_sum = (total_sum + nums[i] * freq[i]) % MOD
            
        return total_sum
        