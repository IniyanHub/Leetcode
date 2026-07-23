class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))

        a = -1
        b = -1
        ans = 0

        for start, end in intervals:

            # Interval already has two selected numbers
            if start <= a:
                continue

            # Interval has only one selected number
            elif start <= b:
                ans += 1
                a = b
                b = end

            # Interval has no selected numbers
            else:
                ans += 2
                a = end - 1
                b = end

        return ans
        