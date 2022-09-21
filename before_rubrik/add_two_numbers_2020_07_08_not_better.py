class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, x: ListNode, y: ListNode) -> ListNode:
        xval = yval = 0
        while x:
            xval += x.val
            x = x.next
        while y:
            yval += y.val
            y = y.next
        z = xval + yval
        head = tail = ListNode(-1)
        while z:
            tail.next = ListNode(z % 10)
            tail = tail.next
            z //= 10
        return head.next

s = Solution()
assert s.addTwoNumbers(ListNode(3), ListNode(5)).val == ListNode(8).val
