class ListNode:
    def __init__(self, val = "none",prev = None, next = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.current.next = ListNode(url, self.current)
        self.current = self.current.next
        
    def back(self, steps: int) -> str:
        i = 1
        while (self.current.prev) and i <= steps:
            print(i)
            self.current = self.current.prev
            print(self.current.val)
            i += 1
        return self.current.val

    def forward(self, steps: int) -> str:
        i = 1
        while (self.current.next) and i <= steps:
            self.current = self.current.next
            i += 1
        return self.current.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)