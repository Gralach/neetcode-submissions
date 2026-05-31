# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stacka = [p]
        stackb = [q]

        while stacka and stackb:
            nodea = stacka.pop()
            nodeb = stackb.pop()
            if not nodea and not nodeb:
                continue
            if (not nodea) or (not nodeb) or (nodea.val != nodeb.val):
                return False
            else:
                stacka.append(nodea.right)
                stacka.append(nodea.left)
                stackb.append(nodeb.right)
                stackb.append(nodeb.left)
        if len(stacka) == len(stackb):
            return True
        return False