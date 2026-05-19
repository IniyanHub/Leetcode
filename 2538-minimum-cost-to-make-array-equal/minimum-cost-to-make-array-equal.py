class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def find_cost(target):
            total = 0
            for i in range(len(nums)):
                total += abs(nums[i] - target) * cost[i]
            return total

        left = min(nums)
        right = max(nums)

        # Binary Search on answer
        while left < right:
            mid = (left + right) // 2

            cost1 = find_cost(mid)
            cost2 = find_cost(mid + 1)

            if cost1 <= cost2:
                right = mid
            else:
                left = mid + 1

        return find_cost(left)
        