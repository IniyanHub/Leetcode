class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        suffixSum = 0
        ans = 0

        for i in range(len(satisfaction) - 1, -1, -1):
            suffixSum += satisfaction[i]

            if suffixSum <= 0:
                break

            ans += suffixSum

        return ans
        