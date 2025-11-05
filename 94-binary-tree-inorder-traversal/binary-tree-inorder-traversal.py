# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        cur = root

        while cur or stack:
            # Go as far left as possible, pushing nodes onto the stack.
            while cur:
                stack.append(cur)
                cur = cur.left

            # No more left children – process the node on top of the stack.
            cur = stack.pop()
            result.append(cur.val)

            # Now explore the right subtree of the popped node.
            cur = cur.right

        return result
        