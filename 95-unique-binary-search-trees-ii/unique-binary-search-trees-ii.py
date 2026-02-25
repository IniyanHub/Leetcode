# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        self.val = val
        self.left = left
        self.right = right

from typing import List

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        """
        Returns all structurally unique BSTs that store values 1..n.
        """
        def build(start: int, end: int) -> List[TreeNode]:
            """Recursively generate all BSTs for the range [start, end]."""
            if start > end:
                return [None]          # empty subtree
            
            trees = []
            for i in range(start, end + 1):  # choose i as root
                # generate left and right subtrees
                left_subtrees = build(start, i - 1)
                right_subtrees = build(i + 1, end)
                
                # combine each left with each right
                for left in left_subtrees:
                    for right in right_subtrees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        trees.append(root)
            return trees
        
        return build(1, n)
        