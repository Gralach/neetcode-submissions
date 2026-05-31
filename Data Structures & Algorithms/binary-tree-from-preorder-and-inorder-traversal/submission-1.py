# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0]) if preorder else None
        checkleft = inorder.index(preorder[0]) if preorder else None
        if root is None:
            return None
        root.left = self.buildTree(preorder[1:checkleft+1], inorder[:checkleft])
        root.right = self.buildTree(preorder[checkleft+1:], inorder[checkleft+1:])
        return root