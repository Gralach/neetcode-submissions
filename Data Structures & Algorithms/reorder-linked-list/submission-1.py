# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head.next, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        # set sentinel node
        prev = slow.next = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            #  1 -> n-1 -> 2
            second.next = temp1
            first.next = second
            # after
            # back to second that is saved
            second = temp2
            first = temp1