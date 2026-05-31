# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None
        while curr:
            # diambil [1,2,3]
            temp = curr.next
            curr.next = prev #[0, None]
            prev = curr # diambil [0, None]
            curr = temp # take temp
        return prev