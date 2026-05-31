# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = deque()
        stack.append(root)

        while stack:
            stackLen = len(stack)
            rightside = None

            for i in range(stackLen):
                node = stack.popleft()
                if node:
                    stack.append(node.left)
                    stack.append(node.right)
                    rightside = node.val
            if rightside:
                res.append(rightside)
        return (res)