# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findMin(root):
            res = root
            while res and res.left:
                res = res.left
            return res

        def remove(root, val):
            if not root:
                return None
            if val > root.val:
                root.right = remove(root.right, val)
            elif val < root.val:
                root.left = remove(root.left, val)
            else:
                if not root.right:
                    root = root.left
                elif not root.left:
                    root = root.right
                else:
                    min_node = findMin(root.right)
                    root.val = min_node.val
                    root.right = remove(root.right, min_node.val)
            return root
        return remove(root, key)