class ListNode:
    def __init__(self, val = 0, next = None):
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
        new_node = ListNode(val)
        temp = self.head.next
        new_node.next = temp
        self.head.next = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        cur = self.head.next
        while cur.next:
            cur = cur.next
        new_node = ListNode(val)
        cur.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return None
        cur = self.head
        for _ in range(index):
            cur = cur.next
        new_node = ListNode(val)
        new_node.next = cur.next
        cur.next = new_node
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