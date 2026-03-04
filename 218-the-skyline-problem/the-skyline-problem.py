class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []

    # Map each left coordinate to the list of (height, right) of buildings starting there
        start_map = defaultdict(list)
        critical = set()                     # all left and right x-coordinates
        for l, r, h in buildings:
            start_map[l].append((h, r))
            critical.add(l)
            critical.add(r)

        xs = sorted(critical)                # sorted critical points
        heap = []                            # max-heap via (-height, right)
        prev_max = 0
        result = []

        for x in xs:
        # Add all buildings that start at x
            if x in start_map:
                for h, r in start_map[x]:
                    heapq.heappush(heap, (-h, r))

        # Remove buildings that are no longer active (right <= x)
            while heap and heap[0][1] <= x:
                heapq.heappop(heap)

        # Current maximum height
            curr_max = -heap[0][0] if heap else 0

        # If the height changes, record a key point
            if curr_max != prev_max:
                result.append([x, curr_max])
                prev_max = curr_max

        return result
        