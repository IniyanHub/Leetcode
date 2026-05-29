class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)

        # Frequency array
        count = [0] * (max_cost + 1)

        # Store frequency
        for cost in costs:
            count[cost] += 1

        ice_creams = 0

        # Buy from cheapest to costly
        for cost in range(1, max_cost + 1):

            if count[cost] > 0:

                # Maximum bars we can buy at this cost
                can_buy = min(count[cost], coins // cost)

                ice_creams += can_buy

                coins -= can_buy * cost

        return ice_creams
        