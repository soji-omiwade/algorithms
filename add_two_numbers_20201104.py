'''
anxiety check: minimal
distraction check: minimal
impatience: high
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def getlistval(l1: ListNode) -> int:
            l1val = 0
            if l1:
                l1val = l1.val
                l1 = l1.next
            return l1val, l1
        res = curr = ListNode()
        carry = 0
        while l1 or l2 or carry:
            l1val, l1 = getlistval(l1)
            l2val, l2 = getlistval(l2)
            curr.next = ListNode((l1val + l2val + carry) % 10)
            curr = curr.next
            carry = (l1val + l2val + carry) // 10
        return res.next

l1 = ListNode(2,ListNode(4, ListNode(3)))
l2 = ListNode(5,ListNode(6, ListNode(4)))
res = Solution().addTwoNumbers(l1, l2)
assert (res.val == 7 and res.next.val == 0 and res.next.next.val == 8 
    and not res.next.next.next)