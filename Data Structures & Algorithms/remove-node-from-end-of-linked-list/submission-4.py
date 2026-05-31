# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nth = head
        while n:
            nth = nth.next
            n -= 1
        copy = ListNode(0, head)
        res = copy
        while nth:
            nth = nth.next
            copy = copy.next
        copy.next = copy.next.next
        return res.next