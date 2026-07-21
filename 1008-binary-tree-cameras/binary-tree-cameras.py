# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.cameras = 0

        def dfs(node):
            if node is None:
                return 2

            left = dfs(node.left)
            right = dfs(node.right)

            if left == 0 or right == 0:
                self.cameras +=1
                return 1
            elif left == 1 or right ==1:
                return 2
            else:
                return 0
        
        num = dfs(root)
        if num ==0:
            self.cameras+=1
        
        return self.cameras


            