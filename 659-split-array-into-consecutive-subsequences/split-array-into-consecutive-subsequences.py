class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = Counter(nums)
        # Map to track the number of subsequences that are currently "waiting" for a specific number
        # need[x] = how many subsequences need 'x' as the next number
        need = defaultdict(int)

        for num in nums:
            # If this number has already been used up by a previous step (starting a chain), skip it
            if count[num] == 0:
                continue
            
            # Consume this number
            count[num] -= 1
            
            # Priority 1: Try to append 'num' to an existing subsequence
            if need[num] > 0:
                need[num] -= 1
                # The subsequence now ends at 'num', so it will wait for 'num + 1'
                need[num + 1] += 1
            
            # Priority 2: Try to start a new subsequence of length 3
            elif count[num + 1] > 0 and count[num + 2] > 0:
                # Consume the next two numbers to form [num, num+1, num+2]
                count[num + 1] -= 1
                count[num + 2] -= 1
                # The subsequence now ends at 'num + 2', so it will wait for 'num + 3'
                need[num + 3] += 1
            
            # Priority 3: Cannot append or start a new valid sequence
            else:
                return False

        return True
        