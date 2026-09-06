class ListNode:
    def __init__(self, val = 0, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        # dummy nodes
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        # connect nodes
        self.head.next = self.tail
        self.tail.prev = self.head
        # helper
        self.size = 0

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False

    def append(self, value: int) -> None:
        temp = self.tail.prev
        new_node = ListNode(value, temp, self.tail)
        self.tail.prev = new_node
        temp.next = new_node
        self.size += 1

    def appendleft(self, value: int) -> None:
        temp = self.head.next
        new_node = ListNode(value, self.head, temp)
        self.head.next = new_node
        temp.prev = new_node
        cur = self.tail.prev
        self.size += 1
        
    def pop(self) -> int:
        if self.size == 0:
            return -1
        value = self.tail.prev.val
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        self.size -= 1
        return value
        

    def popleft(self) -> int:
        if self.size == 0:
            return -1
        value = self.head.next.val
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.size -= 1
        return value
