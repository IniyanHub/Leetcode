class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
    
    # Union-Find setup
        parent = list(range(n))
    
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # path compression
            return parent[x]
    
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
    
    # Check similarity
        def is_similar(a, b):
            diff = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff += 1
                    if diff > 2:
                        return False
            return diff == 0 or diff == 2
    
    # Compare all pairs
        for i in range(n):
            for j in range(i + 1, n):
                if is_similar(strs[i], strs[j]):
                    union(i, j)
    
    # Count unique groups
        groups = set(find(i) for i in range(n))
        return len(groups)
        