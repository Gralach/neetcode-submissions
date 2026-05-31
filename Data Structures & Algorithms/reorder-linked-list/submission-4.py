# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        middle = slow.next
        slow.next = None
        prev = None

        while middle:
            temp = middle.next
            middle.next = prev
            prev = middle
            middle = temp
        
        start = head
        end = prev
        while end:
            temp1, temp2 = start.next, end.next
            # next [2, 8]
            start.next, end.next = end, temp1
            start, end = temp1, temp2