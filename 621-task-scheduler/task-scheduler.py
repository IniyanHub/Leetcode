class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
    
    # 1. Count the frequency of each task
        frequencies = Counter(tasks)
    
    # 2. Find the maximum frequency
        max_freq = max(frequencies.values())
    
    # 3. Count how many tasks have this maximum frequency
    # (e.g., if A is 3 and B is 3, max_count is 2)
        max_count = sum(1 for count in frequencies.values() if count == max_freq)
    
    # 4. Calculate the minimum length required based on the most frequent tasks
    # We have (max_freq - 1) chunks, each of size (n + 1)
    # plus the last chunk which just contains the tasks with max_freq
        part_count = (max_freq - 1) * (n + 1) + max_count
    
    # 5. The result is the max of the calculated length and the total number of tasks
    # (If we have enough unique tasks to fill the idle slots, we don't need extra time)
        return max(part_count, len(tasks))
        