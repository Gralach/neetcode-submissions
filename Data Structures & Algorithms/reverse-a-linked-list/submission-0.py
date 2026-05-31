# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # init prev, cur
        prev, cur = None, head
        # while cur is not None
        while cur:
            # take next link
            nxt = cur.next
            # break next link
            cur.next = prev
            # set the broken up link as prev
            prev = cur
            # update cur with saved next link
            cur = nxt
        return prev