class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        pos = {}

        # Store current position of each person
        for i, person in enumerate(row):
            pos[person] = i

        swaps = 0

        for i in range(0, len(row), 2):
            first = row[i]
            partner = first ^ 1

            # Already sitting together
            if row[i + 1] == partner:
                continue

            swaps += 1

            partner_index = pos[partner]
            second = row[i + 1]

            # Swap partner into the correct position
            row[i + 1], row[partner_index] = row[partner_index], row[i + 1]

            # Update positions
            pos[second] = partner_index
            pos[partner] = i + 1

        return swaps
        