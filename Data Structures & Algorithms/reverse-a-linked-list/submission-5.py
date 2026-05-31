# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        check = head
        prev = None

        while check:
            temp = check.next
            check.next = prev
            prev = check
            check = temp
        return prev