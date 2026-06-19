class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = sorted(Counter(arr).values())

        unique = len(freq)

        for f in freq:
            if k >= f:
                k -= f
                unique -= 1
            else:
                break

        return unique