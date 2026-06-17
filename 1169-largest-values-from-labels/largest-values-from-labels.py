class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        items = sorted(zip(values, labels), reverse=True)

        label_count = defaultdict(int)
        total = 0
        chosen = 0

        for value, label in items:
            if chosen == numWanted:
                break

            if label_count[label] < useLimit:
                total += value
                label_count[label] += 1
                chosen += 1

        return total
        