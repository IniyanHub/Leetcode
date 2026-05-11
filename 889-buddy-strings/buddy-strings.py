class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        # If strings are already equal
        if s == goal:
            # Check for duplicate characters
            return len(set(s)) < len(s)

        # Find positions where characters differ
        diff = []

        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)

        # Exactly two differences needed
        if len(diff) != 2:
            return False

        i, j = diff

        # Check if swapping makes strings equal
        return s[i] == goal[j] and s[j] == goal[i]
        