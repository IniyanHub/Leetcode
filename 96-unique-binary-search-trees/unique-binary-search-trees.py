class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        
        # Base cases
        # Empty tree is considered 1 structure
        dp[0] = 1
        # Single node tree has 1 structure
        dp[1] = 1
        
        # Fill dp table for i from 2 to n
        for i in range(2, n + 1):
            # For a sequence of length i, we pick each number j (1..i) as the root.
            # If j is the root, the left subtree has j-1 nodes, and the right subtree has i-j nodes.
            # The total structures for root j is dp[j-1] * dp[i-j].
            total = 0
            for j in range(1, i + 1):
                total += dp[j - 1] * dp[i - j]
            dp[i] = total
            
        return dp[n]
        