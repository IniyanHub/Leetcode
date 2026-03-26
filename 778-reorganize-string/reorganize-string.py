class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        
        # Max-heap: Python's heapq is a min-heap, so we store negative counts
        # The heap elements are tuples of (-frequency, character)
        max_heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(max_heap)
        
        result = []
        
        # These variables hold the character used in the previous step
        # that is currently in "cooldown". It cannot be used in the immediate next step.
        prev_count = 0
        prev_char = ''
        
        while max_heap:
            # Get the most frequent character available
            freq, char = heapq.heappop(max_heap)
            result.append(char)
            
            # If there was a character in cooldown (prev_count < 0), it can now be
            # added back to the heap because we have placed a different character in between.
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))
            
            # Decrement the frequency of the current character (since we just used it)
            # and put it into cooldown for the next iteration.
            freq += 1
            prev_count = freq
            prev_char = char
        
        # If the result string length is less than the input string length,
        # it means we couldn't place all characters without having adjacent duplicates.
        return "".join(result) if len(result) == len(s) else ""
        