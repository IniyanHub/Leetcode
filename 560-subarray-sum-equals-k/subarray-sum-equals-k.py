class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0

        # prefix_sum : frequency
        freq = {0: 1}

        for num in nums:
            prefix_sum += num

            # We need a previous prefix sum equal to
            # current prefix sum - k
            required = prefix_sum - k

            if required in freq:
                count += freq[required]

            # Store/update frequency of current prefix sum
            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

        return count
        