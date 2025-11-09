# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
     # Both empty → identical
        if p is None and q is None:
            return True
        # One empty, the other not → different structure
        if p is None or q is None:
            return False
        # Different values → not identical
        if p.val != q.val:
            return False
        # Recursively compare left and right sub‑trees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
