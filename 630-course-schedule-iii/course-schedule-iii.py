class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
    
    # Use a Max Heap to store the duration of taken courses.
    # In Python, heapq is a Min Heap, so we store negative values to simulate a Max Heap.
        max_heap = []
        current_time = 0
    
        for duration, last_day in courses:
        # 1. Try to take the current course
            current_time += duration
            heapq.heappush(max_heap, -duration)
        
        # 2. If we exceed the deadline, remove the course with the longest duration
            if current_time > last_day:
            # heappop returns the largest negative number (smallest value), 
            # which corresponds to the largest positive duration.
                longest_duration = -heapq.heappop(max_heap)
                current_time -= longest_duration
            
    # The size of the heap represents the maximum number of courses we can take
        return len(max_heap)
        