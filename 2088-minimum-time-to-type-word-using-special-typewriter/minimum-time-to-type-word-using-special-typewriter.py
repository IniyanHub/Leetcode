class Solution:
    def minTimeToType(self, word: str) -> int:
        time = 0
        current = 0  # 'a'

        for char in word:
            target = ord(char) - ord('a')
            distance = abs(target - current)

            time += min(distance, 26 - distance) + 1

            current = target

        return time
        