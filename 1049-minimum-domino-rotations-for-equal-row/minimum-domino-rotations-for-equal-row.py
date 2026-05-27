class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(x):

            top_rotate = 0
            bottom_rotate = 0

            for i in range(len(tops)):

                # impossible case
                if tops[i] != x and bottoms[i] != x:
                    return float('inf')

                # rotate top
                if tops[i] != x:
                    top_rotate += 1

                # rotate bottom
                if bottoms[i] != x:
                    bottom_rotate += 1

            return min(top_rotate, bottom_rotate)

        ans = min(check(tops[0]), check(bottoms[0]))

        return -1 if ans == float('inf') else ans
        