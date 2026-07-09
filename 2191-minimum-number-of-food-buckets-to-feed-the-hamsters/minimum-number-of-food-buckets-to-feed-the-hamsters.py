class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        s = list(hamsters)
        n = len(s)
        buckets = 0

        for i in range(n):
            if s[i] != 'H':
                continue

            # Already fed by a bucket on the left
            if i > 0 and s[i - 1] == 'B':
                continue

            # Prefer placing a bucket on the right
            if i + 1 < n and s[i + 1] == '.':
                s[i + 1] = 'B'
                buckets += 1

            # Otherwise place on the left
            elif i > 0 and s[i - 1] == '.':
                s[i - 1] = 'B'
                buckets += 1

            # Impossible to feed this hamster
            else:
                return -1

        return buckets
        