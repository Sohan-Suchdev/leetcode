# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.global_max = -float('inf')

        def dfs(node):
            if not node:
                return 0

            left_best = max(0, dfs(node.left))
            right_best = max(0, dfs(node.right))

            current_v_shape = node.val + left_best + right_best
            self.global_max = max(self.global_max, current_v_shape)

            return node.val + max(left_best, right_best)

        dfs(root)

        return self.global_max