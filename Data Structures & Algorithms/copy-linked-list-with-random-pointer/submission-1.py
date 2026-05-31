"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copytomap = {None: None}
        cur = head
        while cur:
            copy = Node(cur.val)
            copytomap[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = copytomap[cur]
            copy.next = copytomap[cur.next]
            copy.random = copytomap[cur.random]
            cur = cur.next
        return copytomap[head]