class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)

        # Store all indices for each value
        positions = defaultdict(list)

        for i, num in enumerate(nums):
            positions[num].append(i)

        answer = []

        for q in queries:
            value = nums[q]
            indices = positions[value]

            # If only one occurrence exists
            if len(indices) == 1:
                answer.append(-1)
                continue

            # Find position of q in indices list
            idx = bisect_left(indices, q)

            # Previous and next same-value indices (circular)
            prev_idx = indices[idx - 1]
            next_idx = indices[(idx + 1) % len(indices)]

            # Circular distances
            d1 = abs(q - prev_idx)
            d1 = min(d1, n - d1)

            d2 = abs(q - next_idx)
            d2 = min(d2, n - d2)

            answer.append(min(d1, d2))

        return answer
        