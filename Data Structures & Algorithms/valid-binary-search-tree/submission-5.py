# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = deque()
        stack.append([root, float("-inf"), float("inf")])

        while stack:
            stackLen = len(stack)
            for i in range(stackLen):
                node, left, right = stack.popleft()
                if not(left < node.val < right):
                    return False
                if node.left:
                    stack.append([node.left, left, node.val])
                if node.right:
                    stack.append([node.right, node.val, right])
                print(stack)
        return True