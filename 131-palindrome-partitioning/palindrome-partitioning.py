class Solution:
    def partition(self, s: str) -> list[list[str]]:
        ans = []

        def backtrack(start, path):
            if start == len(s):
                ans.append(path.copy())
                return

            for end in range(start, len(s)):
                sub = s[start:end + 1]

                if sub == sub[::-1]:
                    path.append(sub)
                    backtrack(end + 1, path)
                    path.pop()

        backtrack(0, [])
        return ans
        