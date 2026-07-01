class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        even_sum = 0
        odd_sum = 0

        for i, x in enumerate(nums):
            if i % 2 == 0:
                even_sum += x
            else:
                odd_sum += x

        left_even = 0
        left_odd = 0
        ans = 0

        for i, x in enumerate(nums):

            # Remove current element from right sums
            if i % 2 == 0:
                even_sum -= x
            else:
                odd_sum -= x

            # After removal, right side changes parity
            if left_even + odd_sum == left_odd + even_sum:
                ans += 1

            # Add current element to left sums
            if i % 2 == 0:
                left_even += x
            else:
                left_odd += x

        return ans
        