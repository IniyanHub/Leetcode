class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for i in range(len(equations)):
            u, v = equations[i]
            val = values[i]
            
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
                
            # Add edge u -> v with weight val (u / v = val)
            graph[u].append((v, val))
            # Add edge v -> u with weight 1/val (v / u = 1/val)
            graph[v].append((u, 1.0 / val))
        
        def dfs(node, target, visited):
            # Base case: reached the target node
            if node == target:
                return 1.0
            
            visited.add(node)
            
            # Explore neighbors
            for neighbor, weight in graph.get(node, []):
                if neighbor not in visited:
                    # Recursively find the product from neighbor to target
                    product = dfs(neighbor, target, visited)
                    if product != -1.0:
                        return weight * product
            
            # If no path found
            return -1.0
        
        results = []
        for c, d in queries:
            # Case 1: Either variable is undefined
            if c not in graph or d not in graph:
                results.append(-1.0)
            # Case 2: Same variable
            elif c == d:
                results.append(1.0)
            # Case 3: Find path
            else:
                visited = set()
                results.append(dfs(c, d, visited))
                
        return results
        