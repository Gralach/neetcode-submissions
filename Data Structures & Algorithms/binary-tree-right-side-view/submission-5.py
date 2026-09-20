# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        if not root:
            return []
        q.append(root)
        res.append(root.val)

        level = 0
        while q:
            q_len = len(q)
            temp = False
            for _ in range(q_len):
                cur = q.popleft()
                if cur.right:
                    q.append(cur.right)
                    if not temp:
                        res.append(cur.right.val)                        
                        temp = True
                if cur.left:
                    q.append(cur.left)
                    if not temp:
                        res.append(cur.left.val)
                        temp = True
        return res