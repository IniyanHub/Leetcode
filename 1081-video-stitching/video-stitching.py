class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        max_reach = [0] * (time + 1)

        for start, end in clips:
            if start <= time:
                max_reach[start] = max(max_reach[start], min(end, time))

        ans = 0
        cur_end = 0
        next_end = 0

        for i in range(time):
            next_end = max(next_end, max_reach[i])

            if i == cur_end:
                if next_end <= i:
                    return -1
                ans += 1
                cur_end = next_end

                if cur_end >= time:
                    return ans

        return -1

        