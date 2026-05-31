# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        stack = deque()
        stack.append([root.val, root])

        while stack:
            stackLen = len(stack)
            for i in range(stackLen):
                maxs, node = stack.popleft()

                if node:
                    if node.val >= maxs:
                        res += 1
                    maxs = max(node.val, maxs)
                    stack.append([maxs, node.left])
                    stack.append([maxs, node.right])
        return res