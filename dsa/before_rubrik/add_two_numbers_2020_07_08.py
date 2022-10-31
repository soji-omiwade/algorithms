class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, x: ListNode, y: ListNode) -> ListNode:
        tail = head = ListNode(-1)
        carry = 0
        while carry != 0 or x or y:
            xval = 0
            if x:
                xval = x.val
                x = x.next
            yval = 0
            if y:
                yval = y.val
                y = y.next
            tail.next = ListNode((xval + yval + carry) % 10)
            tail = tail.next
            carry = int(xval + yval + carry > 9)
        return head.next

s = Solution()
assert s.addTwoNumbers(ListNode(3), ListNode(5)).val == ListNode(8).val
