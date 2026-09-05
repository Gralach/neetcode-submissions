class ListNode:
    def __init__(self, val = 0, next= None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.size = 0        

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        cur = self.head.next
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        cur = self.head.next
        new = ListNode(val)
        new.next = cur
        self.head.next = new
        self.size += 1

    def addAtTail(self, val: int) -> None:
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = ListNode(val, None)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return None
        cur = self.head
        for _ in range(index):
            cur = cur.next
        temp = cur.next
        new = ListNode(val)
        new.next = temp
        cur.next = new
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return None
        cur = self.head
        for _ in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)