class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-x for x in piles]
        heapq.heapify(heap)

        for _ in range(k):
            largest = -heapq.heappop(heap)
            largest -= largest // 2      # Remaining = ceil(largest/2)
            heapq.heappush(heap, -largest)

        return -sum(heap)
        