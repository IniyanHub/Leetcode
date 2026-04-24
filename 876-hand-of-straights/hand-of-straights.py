class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for x in sorted(count):
            while count[x] > 0:   # process each occurrence
                for i in range(groupSize):
                    if count[x + i] <= 0:   # strict check
                        return False
                    count[x + i] -= 1

        return True
        