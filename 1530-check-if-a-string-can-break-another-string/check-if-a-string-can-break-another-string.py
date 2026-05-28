class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)

        # Check if s1 can break s2
        if all(s1[i] >= s2[i] for i in range(len(s1))):
            return True

        # Check if s2 can break s1
        if all(s2[i] >= s1[i] for i in range(len(s1))):
            return True

        return False
        