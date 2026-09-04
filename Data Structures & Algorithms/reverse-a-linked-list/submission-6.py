# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stay, res = head, head
        items = []

        while head:
            items.append(head.val)
            head = head.next
        for i in range(len(items) -1, -1, -1):
            stay.val = items[i]
            stay = stay.next
        return res