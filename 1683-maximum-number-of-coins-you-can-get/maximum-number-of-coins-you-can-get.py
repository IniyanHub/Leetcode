class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()

        left = 0
        right = len(piles) - 1
        ans = 0

        while left < right:
            right -= 1          # Your pile (second largest)
            ans += piles[right]

            right -= 1          # Alice's largest pile
            left += 1           # Bob's smallest pile

        return ans
        