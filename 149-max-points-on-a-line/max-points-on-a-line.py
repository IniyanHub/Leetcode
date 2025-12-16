from typing import List
from collections import defaultdict
from math import gcd
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        answer = 0

        for i in range(n):
            slopes = defaultdict(int)   # (dx, dy) -> count
            duplicates = 0
            local_max = 0

            xi, yi = points[i]

            for j in range(i + 1, n):
                xj, yj = points[j]
                dx = xj - xi
                dy = yj - yi

                # same point
                if dx == 0 and dy == 0:
                    duplicates += 1
                    continue

                # reduce the direction vector
                g = gcd(dx, dy)          # gcd is always non‑negative
                dx //= g
                dy //= g

                # canonical representation: make dx non‑negative
                if dx < 0:
                    dx = -dx
                    dy = -dy
                elif dx == 0:            # vertical line
                    dy = 1               # (0,1) uniquely represents vertical
                elif dy == 0:            # horizontal line
                    dx = 1               # (1,0) uniquely represents horizontal

                slopes[(dx, dy)] += 1
                local_max = max(local_max, slopes[(dx, dy)])

            # +1 for point i itself, +duplicates for overlapping points
            answer = max(answer, local_max + duplicates + 1)

        return answer
        