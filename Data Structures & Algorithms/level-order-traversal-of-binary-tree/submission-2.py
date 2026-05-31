# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # can use breadth first search
        result = []
        stack = deque()
        stack.append(root)
        while stack:
            stackLen = len(stack)
            temp = []
            for i in range(stackLen):
                node = stack.popleft()
                if node:
                    stack.append(node.left)
                    stack.append(node.right)
                    temp.append(node.val)
            if temp:
                result.append(temp)
        return result