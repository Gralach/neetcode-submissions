# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head.next
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        middle = slow.next
        prev = slow.next = None
        # reverse linkedlist
        while middle:
            temp = middle.next
            middle.next = prev
            prev = middle
            middle = temp
        first, second = head, prev
        while second:
            # [2, 4] [8, 6]
            temp1, temp2 = first.next, second.next # [4] [6]
            first.next, second.next = second, temp1 # [2, 8, 6] [8, 4]
            first, second = temp1, temp2
