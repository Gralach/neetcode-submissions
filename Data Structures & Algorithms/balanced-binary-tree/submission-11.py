# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        def inorder_height(root):
            if not root:
                return 1
            height_left, height_right = inorder_height(root.left), inorder_height(root.right)
            if abs(height_left - height_right) > 1:
                self.res = False
            return 1 + max(height_left, height_right)
        inorder_height(root)
        return self.res