class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        max_heap = []

        stations.append([target, 0])

        fuel = startFuel
        stops = 0

        for position, gas in stations:

            # If we can't reach this station,
            # refuel from the best station we've passed.
            while fuel < position:
                if not max_heap:
                    return -1

                fuel += -heapq.heappop(max_heap)
                stops += 1

            heapq.heappush(max_heap, -gas)

        return stops
        