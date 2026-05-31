# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        move = res
        carry = 0
        while l1 or l2 or carry:
            val1, val2 = l1.val if l1 else 0, l2.val if l2 else 0
            temp = val1 + val2 + carry
            value, carry = temp % 10, temp //10
            move.next = ListNode(value)
            l1, l2 = l1.next if l1 else 0, l2.next if l2 else 0
            move = move.next
        return res.next