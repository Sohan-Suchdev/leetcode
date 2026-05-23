# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            if not root:
                return []

            ret = []
            if root.left:
                ret.extend(inorder(root.left))
            ret.append(root.val)
            if root.right:
                ret.extend(inorder(root.right))
            return ret
               
        arr = inorder(root)
        return arr[k-1]

