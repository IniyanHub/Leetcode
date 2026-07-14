class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        max_heap = []
        minimum = float("inf")

        # Make every number even
        for num in nums:
            if num % 2 == 1:
                num *= 2
            minimum = min(minimum, num)
            heapq.heappush(max_heap, -num)

        ans = float("inf")

        while True:
            maximum = -heapq.heappop(max_heap)
            ans = min(ans, maximum - minimum)

            # Can't reduce odd numbers further
            if maximum % 2 == 1:
                break

            maximum //= 2
            minimum = min(minimum, maximum)
            heapq.heappush(max_heap, -maximum)

        return ans
        