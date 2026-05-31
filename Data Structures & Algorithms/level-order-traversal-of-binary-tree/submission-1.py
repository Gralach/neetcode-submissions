# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        stack = deque([])
        stack.append(root)
        while stack:
            stackLen = len(stack)
            temp = []
            for i in range(stackLen):
                node = stack.popleft()
                if node:
                    temp.append(node.val)
                    stack.append(node.left)
                    stack.append(node.right)
            if temp:
                res.append(temp)
        return res