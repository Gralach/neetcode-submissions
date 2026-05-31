# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res1, res2 = l1, l2
        str1, str2 = "" ,""

        while res1 or res2:
            if res1:
                str1 = str(res1.val) + str1
                res1 = res1.next
            if res2:
                str2 = str(res2.val) + str2
                res2 = res2.next
        
        summation = str(eval(f"{str1}+{str2}"))
        sumlist = ListNode(0, None)
        final = sumlist

        for a in range(len(summation) - 1, -1 , -1):
            sumlist.next = ListNode(int(summation[a]), None)
            sumlist = sumlist.next
        
        return final.next
            