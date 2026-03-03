class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
    
        for num in nums:
        # Push the current number onto the heap
            heapq.heappush(heap, num)
        
        # If the heap size exceeds k, pop the smallest element
        # This ensures the heap always contains the k largest elements seen so far
            if len(heap) > k:
                heapq.heappop(heap)
            
    # The root of the heap (index 0) is the kth largest element
        return heap[0]
        