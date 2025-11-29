# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first, second = None, None
        # Initialize pointer for the previous node in in-order traversal
        prev = None
        
        # Use a stack for iterative in-order traversal
        stack = []
        node = root
        
        while stack or node:
            # Go as far left as possible
            while node:
                stack.append(node)
                node = node.left
            
            # Process the node
            node = stack.pop()
            
            # Check for BST property violation
            if prev and prev.val > node.val:
                # If this is the first violation, mark both nodes
                if not first:
                    first = prev
                # If it's the second violation, or the first one,
                # mark the current node as the second
                second = node
            
            # Update the previous node
            prev = node
            
            # Move to the right subtree
            node = node.right
        
        # Swap the values of the two identified nodes
        first.val, second.val = second.val, first.val

        