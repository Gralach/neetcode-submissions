# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sentinel = head
        prev = None
        while sentinel:
            temp = sentinel.next
            sentinel.next = prev
            prev = sentinel
            sentinel = temp
        titit, count = None, 1
        while prev:
            if count == n:
                prev = prev.next
                count += 1
            else:
                temp = prev.next
                prev.next = titit
                titit = prev
                print(titit.val)
                prev = temp
                count += 1
        return titit
