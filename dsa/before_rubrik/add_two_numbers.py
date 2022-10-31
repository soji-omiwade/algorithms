# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = None
        c = 0
        while True:
            if not l1 and not l2: break
            val = c + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            x, c = val % 10, val // 10
            w = ListNode(x)
            if not res: res = tail = w
            else:
                tail.next = w
                tail = w
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if c: tail.next = ListNode(c)
        return res