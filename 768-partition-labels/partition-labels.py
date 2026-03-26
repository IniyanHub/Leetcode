class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {c: i for i, c in enumerate(s)}
        
        result = []
        start = 0  # Start index of the current partition
        end = 0    # End index of the current partition
        
        for i, c in enumerate(s):
            # Extend the current partition to at least the last occurrence of s[i]
            end = max(end, last_occurrence[c])
            
            # If we've reached the end of the current partition
            if i == end:
                # Calculate the length and add to results
                result.append(i - start + 1)
                # Move the start to the next character
                start = i + 1
                
        return result
        