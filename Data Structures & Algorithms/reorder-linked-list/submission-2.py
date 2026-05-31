# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first phase (reverse)
        rabbit, turtle = head.next, head
        while rabbit and rabbit.next:
            turtle = turtle.next
            rabbit = rabbit.next.next
        copy, prev = turtle.next, None
        turtle.next = None
        
        while copy:
            temp = copy.next
            copy.next = prev
            prev = copy
            copy = temp
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
            