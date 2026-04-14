class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        visited = set()
        res = []

        def dfs(node):
            for x in range(k):
                nei = node + str(x)
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei[1:])
                    res.append(str(x))

        start = "0" * (n - 1)
        dfs(start)
    
        return "".join(res) + start
        