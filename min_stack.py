class MinStack:
    class ListNode:
        def __init__(self, val):
            self.val = val
            self.next = None
            
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = MinStack.ListNode(None)
        self.tail = MinStack.ListNode(None)
        self.head.next = self.tail
        self.tail.best_min_val = float("inf")

    def push(self, x: int) -> None:
        v = MinStack.ListNode(x)
        v.next = self.head.next
        self.head.next = v
        v.best_min_val = min(v.val, v.next.best_min_val)

    def pop(self) -> None:
        self.head.next = self.head.next.next

    def top(self) -> int:
        return self.head.next.val

    def getMin(self) -> int:
        return self.head.next.best_min_val

ms = MinStack()
ms.push(2)
ms.push(0)
ms.push(93)
ms.push(42)
ms.push(43)
assert ms.getMin() == 0
assert ms.pop() is None
assert ms.top() == 42
assert ms.getMin() == 0
