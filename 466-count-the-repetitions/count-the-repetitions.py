class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        len1 = len(s1)
        len2 = len(s2)
        
        # Basic edge case checks
        if len1 == 0 or len2 == 0 or n1 == 0 or n2 == 0:
            return 0
        
        # Optimization: if s2 contains characters not in s1, it's impossible
        if not set(s2).issubset(set(s1)):
            return 0

        # repeatCount[i]: number of times s2 can be fully matched when scanning s1
        #                  starting from the i-th character of s2.
        # nextIndex[i]:   the index in s2 we end up at after scanning s1
        #                  starting from the i-th character of s2.
        repeatCount = [0] * len2
        nextIndex = [0] * len2
        
        # Precompute repeatCount and nextIndex for all possible starting indices in s2
        for i in range(len2):
            curr_s2_idx = i
            count = 0
            for char in s1:
                if char == s2[curr_s2_idx]:
                    curr_s2_idx += 1
                    if curr_s2_idx == len2:
                        curr_s2_idx = 0
                        count += 1
            repeatCount[i] = count
            nextIndex[i] = curr_s2_idx
            
        # Simulation variables
        # visited[i] will store the iteration number (k) when we were at state i
        # count_at_state[i] will store the total count of s2 found at that iteration
        visited = [-1] * len2
        count_at_state = [0] * len2
        
        curr_state = 0
        total_count = 0
        k = 0 # Number of s1 blocks processed
        
        while k < n1:
            # Cycle Detection
            if visited[curr_state] != -1:
                # We have seen this state before. A cycle exists.
                # The cycle started at iteration 'visited[curr_state]'
                # We are currently at iteration 'k'
                cycle_start_iteration = visited[curr_state]
                cycle_length = k - cycle_start_iteration
                
                # How many s2's were found during one full cycle?
                count_gain_per_cycle = total_count - count_at_state[curr_state]
                
                # How many iterations remain?
                remaining_iters = n1 - k
                
                # How many full cycles can we fit in the remaining iterations?
                num_cycles = remaining_iters // cycle_length
                
                # Add the counts from the repeated cycles
                total_count += num_cycles * count_gain_per_cycle
                
                # Fast forward k by the number of iterations covered by these cycles
                k += num_cycles * cycle_length
                
                # Reset visited to prevent re-triggering the cycle logic for the tail
                # We will now just process the remaining few iterations linearly
                visited = [-1] * len2
                
                # If we have consumed all iterations, break
                if k >= n1:
                    break
            
            # Record the current state
            visited[curr_state] = k
            count_at_state[curr_state] = total_count
            
            # Process the current s1 block
            total_count += repeatCount[curr_state]
            curr_state = nextIndex[curr_state]
            k += 1
            
        # total_count is the max number of s2's in str1.
        # We want max m such that [s2, n2 * m] is in str1.
        # This means n2 * m <= total_count.
        return total_count // n2
        