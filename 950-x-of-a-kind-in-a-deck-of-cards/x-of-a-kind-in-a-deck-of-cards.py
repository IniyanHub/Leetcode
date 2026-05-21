class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        freq = Counter(deck)

        # Find GCD of all frequencies
        g = reduce(gcd, freq.values())

        # Partition is possible only if GCD > 1
        return g > 1
        