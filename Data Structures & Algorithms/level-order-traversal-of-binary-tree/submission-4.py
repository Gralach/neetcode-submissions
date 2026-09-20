# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        res = []

        if not root:
            return res
        
        queue.append(root)
        res.append([root.val])
        level = 0
        
        while queue:
            temp = []
            q_len = len(queue)
            while q_len:
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                    temp.append(cur.left.val)
                if cur.right:
                    queue.append(cur.right)
                    temp.append(cur.right.val)
                q_len -= 1
            if temp:
                res.append(temp)
            level += 1
        return res