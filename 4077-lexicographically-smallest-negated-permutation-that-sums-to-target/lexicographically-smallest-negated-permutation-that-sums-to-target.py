class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:
        total = n * (n + 1) // 2

        # Impossible conditions
        if abs(target) > total:
            return []

        # target and total must have same parity
        if (total - target) % 2 != 0:
            return []

        # Sum of numbers that should be negative
        need = (total - target) // 2

        negative = set()

        # Greedily take largest numbers
        for x in range(n, 0, -1):
            if x <= need:
                negative.add(x)
                need -= x

        # Build lexicographically smallest array
        ans = []

        # Negative numbers in descending order
        for x in range(n, 0, -1):
            if x in negative:
                ans.append(-x)

        # Positive numbers in ascending order
        for x in range(1, n + 1):
            if x not in negative:
                ans.append(x)

        return ans
        