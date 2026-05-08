class Solution:
    def minPartitionScore(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Prefix sums
        pre = [0] * (n + 1)

        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]

        INF = 10**30

        dp_prev = [INF] * (n + 1)
        dp_prev[0] = 0

        # Line:
        # y = m*x + b
        class Line:
            def __init__(self, m, b):
                self.m = m
                self.b = b

            def value(self, x):
                return self.m * x + self.b

        # Check useless line
        def bad(l1, l2, l3):
            return ((l3.b - l1.b) * (l1.m - l2.m)
                    <= (l2.b - l1.b) * (l1.m - l3.m))

        for _ in range(k):

            dp_curr = [INF] * (n + 1)

            hull = deque()

            # Add first line from j=0
            m = -pre[0]
            b = dp_prev[0] + (pre[0] * pre[0] - pre[0]) // 2

            hull.append(Line(m, b))

            for i in range(1, n + 1):

                x = pre[i]

                # Query best line
                while len(hull) >= 2 and \
                      hull[0].value(x) >= hull[1].value(x):
                    hull.popleft()

                best = hull[0].value(x)

                dp_curr[i] = (
                    (x * x + x) // 2
                    + best
                )

                # Create new line for this i
                if dp_prev[i] < INF:

                    m = -pre[i]
                    b = dp_prev[i] + \
                        (pre[i] * pre[i] - pre[i]) // 2

                    new_line = Line(m, b)

                    while len(hull) >= 2 and \
                          bad(hull[-2], hull[-1], new_line):
                        hull.pop()

                    hull.append(new_line)

            dp_prev = dp_curr

        return dp_prev[n]
        