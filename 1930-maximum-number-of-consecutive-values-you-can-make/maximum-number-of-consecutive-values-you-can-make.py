class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()

        max_value = 0

        for coin in coins:
            if coin > max_value + 1:
                break

            max_value += coin

        return max_value + 1
        