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
        hashmap = {None: None}
        copy = head
        while copy:
            hashmap[copy] = Node(copy.val)
            copy = copy.next
        res = hashmap[head]
        while head:
            cur = hashmap[head]
            cur.next = hashmap[head.next]
            cur.random = hashmap[head.random]
            head = head.next
        return res