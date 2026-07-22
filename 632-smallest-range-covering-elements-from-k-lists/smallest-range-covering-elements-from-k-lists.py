class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        current_max = float('-inf')

        # Initialize heap with the first element of each list
        for i, arr in enumerate(nums):
            heapq.heappush(heap, (arr[0], i, 0))
            current_max = max(current_max, arr[0])

        start, end = 0, float('inf')

        while True:
            current_min, list_idx, elem_idx = heapq.heappop(heap)

            if current_max - current_min < end - start:
                start, end = current_min, current_max

            # If we've reached the end of one list, stop
            if elem_idx + 1 == len(nums[list_idx]):
                break

            next_val = nums[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
            current_max = max(current_max, next_val)

        return [start, end]
        