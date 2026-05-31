# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            # [0, 1, 2, 3]
            temp = head.next # [1,2,3]
            head.next = prev # [0, None]
            prev = head # [0, None]
            head = temp
        return prev