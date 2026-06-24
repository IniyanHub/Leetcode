class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False

        odd_count = sum(freq % 2 for freq in Counter(s).values())

        return odd_count <= k
        