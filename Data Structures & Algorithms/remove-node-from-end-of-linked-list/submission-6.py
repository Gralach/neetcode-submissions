# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        moved = head
        while n:
            moved = moved.next
            n -=1
        copy = ListNode()
        copy.next = head
        res = copy
        while moved:
            copy = copy.next
            moved = moved.next
        copy.next = copy.next.next
        return res.next