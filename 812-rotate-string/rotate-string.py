class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        # goal must appear in s+s
        return goal in (s + s)
        