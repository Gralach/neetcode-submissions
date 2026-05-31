# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        
        stack = deque([])
        stack.append([root, root.val])
        while stack:
            stackLen = len(stack)
            # temp = []
            for i in range(stackLen):
                node, prevMax = stack.popleft()
                if node:
                    if node.val >= prevMax:
                        self.res += 1
                        # prevMax = max(prevMax, node.val)
                        prevMax = node.val
                    stack.append([node.left, prevMax])
                    stack.append([node.right, prevMax])
        return(self.res)