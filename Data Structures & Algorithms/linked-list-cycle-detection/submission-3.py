# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        rabbit, turtle = head.next, head

        while rabbit and rabbit.next:
            if rabbit == turtle:
                return True
            rabbit = rabbit.next.next
            turtle = turtle.next
        return False