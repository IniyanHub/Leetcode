class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

    # pos[d] stores the indices (in order) where digit d appears in s
        pos = [deque() for _ in range(10)]
        for i, ch in enumerate(s):
            pos[int(ch)].append(i)

        for ch in t:
            d = int(ch)
            if not pos[d]:
                return False          # count mismatch

            idx = pos[d][0]           # leftmost remaining occurrence of d

        # Check if any smaller digit lies to the left of this occurrence
            for smaller in range(d):
                if pos[smaller] and pos[smaller][0] < idx:
                    return False

        # Use this digit
            pos[d].popleft()

        return True
        