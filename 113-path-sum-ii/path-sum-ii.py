# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        result = []

        def dfs(node, current_path, remaining_sum):
            # Base case: if the node is null, this path is invalid.
            if not node:
                return

            # Add the current node's value to the path and update the remaining sum.
            current_path.append(node.val)
            new_remaining_sum = remaining_sum - node.val

            # Check if it's a leaf node and if the path sum matches the target.
            if not node.left and not node.right:
                if new_remaining_sum == 0:
                    # Found a valid path. Add a copy of it to the result.
                    # We must add a copy, not the reference, because current_path
                    # will be modified during backtracking.
                    result.append(list(current_path))
            else:
                # If not a leaf, continue searching in the subtrees.
                dfs(node.left, current_path, new_remaining_sum)
                dfs(node.right, current_path, new_remaining_sum)

            # Backtrack: remove the current node's value from the path
            # before returning to the parent node's call. This is crucial
            # for exploring other branches correctly.
            current_path.pop()

        dfs(root, [], targetSum)
        return result

        