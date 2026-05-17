class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = target

        # To track whether target values can be formed
        found_a = found_b = found_c = False

        for x, y, z in triplets:

            # Ignore triplets that exceed target
            if x > a or y > b or z > c:
                continue

            # Check matching values
            if x == a:
                found_a = True
            if y == b:
                found_b = True
            if z == c:
                found_c = True

        return found_a and found_b and found_c
        