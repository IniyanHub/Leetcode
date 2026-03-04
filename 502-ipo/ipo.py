class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        
        # Max-heap to store profits of affordable projects. 
        # Since Python only has a Min-Heap, we store negative values to simulate a Max-Heap.
        max_heap = []
        
        # Pointer to iterate through the sorted projects
        current_project_index = 0
        n = len(projects)
        
        for _ in range(k):
            # Add all projects that we can afford with the current capital 'w'
            while current_project_index < n and projects[current_project_index][0] <= w:
                # Push negative profit onto the heap
                heapq.heappush(max_heap, -projects[current_project_index][1])
                current_project_index += 1
            
            # If there are no affordable projects, we cannot proceed further
            if not max_heap:
                break
            
            # Select the project with the maximum profit
            # (It is the smallest negative number, i.e., -max_profit)
            max_profit = -heapq.heappop(max_heap)
            
            # Add the profit to our total capital
            w += max_profit
            
        return w
        