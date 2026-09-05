class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)
    
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        cur = self.head.next
        for _ in range(index):
            cur = cur.next
        return cur.val

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        self.size += 1

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        self.size += 1

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        cur = self.head
        for _ in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        cur = self.head.next
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res