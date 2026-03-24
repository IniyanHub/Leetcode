class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        if not target:
            return 0
        
        n = len(target)
        
        # Preprocess target to get character counts
        target_counts = [0] * 26
        for char in target:
            target_counts[ord(char) - ord('a')] += 1
            
        # Convert stickers to counts (only keeping relevant chars)
        sticker_counts = []
        for s in stickers:
            cnt = [0] * 26
            for char in s:
                idx = ord(char) - ord('a')
                # We only care about characters that appear in target
                if target_counts[idx] > 0:
                    cnt[idx] += 1
            if sum(cnt) > 0:
                sticker_counts.append(cnt)
                
        # Check for impossibility: if any char in target is not in any sticker
        # Note: We have infinite stickers, so we just check for existence (>0), not total count.
        total_supply = [0] * 26
        for cnt in sticker_counts:
            for i in range(26):
                total_supply[i] += cnt[i]
        
        for i in range(26):
            if target_counts[i] > 0 and total_supply[i] == 0:
                return -1

        # BFS initialization
        q = deque([0])
        visited = [False] * (1 << n)
        visited[0] = True
        steps = 0
        target_mask = (1 << n) - 1
        
        # Memoization for state transitions
        memo = {}

        while q:
            # Process all nodes at the current step level
            for _ in range(len(q)):
                curr_mask = q.popleft()
                
                # If we have formed the target, return the number of steps
                if curr_mask == target_mask:
                    return steps
                
                # Compute transitions if not already computed
                if curr_mask not in memo:
                    memo[curr_mask] = []
                    for s_cnt in sticker_counts:
                        # Copy sticker counts as we consume them
                        remaining = list(s_cnt)
                        next_mask = curr_mask
                        
                        # Try to fill missing characters in target
                        for i in range(n):
                            # Check if i-th bit is 0 (not yet formed)
                            if not (next_mask >> i) & 1:
                                char_idx = ord(target[i]) - ord('a')
                                if remaining[char_idx] > 0:
                                    remaining[char_idx] -= 1
                                    next_mask |= (1 << i)
                        
                        memo[curr_mask].append(next_mask)
                
                # Explore neighbors
                for next_mask in memo[curr_mask]:
                    if not visited[next_mask]:
                        visited[next_mask] = True
                        q.append(next_mask)
            
            steps += 1
            
        return -1
        