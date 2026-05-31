# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        check1, check2 = l1, l2
        int1, int2 = "", ""

        while check1 or check2:
            if check1:
                int1 = str(check1.val) + int1
                check1 = check1.next
            elif check2:
                int2 = str(check2.val) + int2
                check2 = check2.next
        total = eval(f"{int1} + {int2}")
        sums = ListNode()
        res = sums
        for i in str(total)[::-1]:
            sums.next = ListNode(int(i))
            sums = sums.next
        return res.next