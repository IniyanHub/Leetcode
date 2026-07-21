class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        reach = [0] * (n + 1)

        # Build maximum reach for every left endpoint
        for i in range(n + 1):
            left = max(0, i - ranges[i])
            right = min(n, i + ranges[i])
            reach[left] = max(reach[left], right)

        taps = 0
        curr_end = 0
        farthest = 0

        for i in range(n + 1):
            if i > farthest:
                return -1

            farthest = max(farthest, reach[i])

            if i == curr_end:
                if curr_end == n:
                    break
                taps += 1
                curr_end = farthest

        return taps
        