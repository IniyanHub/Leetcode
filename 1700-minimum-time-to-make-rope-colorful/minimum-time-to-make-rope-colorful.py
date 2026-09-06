class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0

        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:

                # Remove the balloon with smaller removal time
                total += min(neededTime[i], neededTime[i - 1])

                # Keep the balloon with larger removal time
                neededTime[i] = max(neededTime[i], neededTime[i - 1])

        return total
        