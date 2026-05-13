class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = []
        
        # Store ratio and quality
        for q, w in zip(quality, wage):
            workers.append((w / q, q))
        
        # Sort by ratio
        workers.sort()
        
        max_heap = []
        quality_sum = 0
        answer = float('inf')
        
        for ratio, q in workers:
            
            # Add current quality
            heapq.heappush(max_heap, -q)
            quality_sum += q
            
            # Keep only k workers
            if len(max_heap) > k:
                quality_sum += heapq.heappop(max_heap)
            
            # Calculate cost when exactly k workers
            if len(max_heap) == k:
                cost = quality_sum * ratio
                answer = min(answer, cost)
        
        return answer
        