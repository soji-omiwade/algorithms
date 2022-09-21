# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __eq__(self, lp):
        p1 = self
        p2 = lp
        while p1 and p2 and p1.val == p2.val:
            p1 = p1.next
            p2 = p2.next
        if not p1 and not p2:
            return True
        return False
    def __str__(self):
        res = []
        p = self
        while p:
            res += [str(p.val)]
            p = p.next
        return super().__str__() + ': ' + "-->".join(res)
l1 = ListNode(1, ListNode(9, ListNode(3)))
l1_2 = ListNode(1, ListNode(9, ListNode(3)))
assert l1 == l1_2
l1 = ListNode(1, ListNode(9, ListNode(3)))
l1_2 = ListNode(10, ListNode(9, ListNode(3)))
assert l1 != l1_2
l1 = ListNode(1, ListNode(9, ListNode(3)))
l1_2 = ListNode(1, ListNode(9))
assert l1 != l1_2

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #create a head ListNode outside the while so we dont
        #have an if in the while that executes just one time!
        head = tail = ListNode(-1)
        carry = 0
        while True:
            #exit while if done
            if carry == 0 and not l1 and not l2:
                break
            x = 0
            if l1:
                x = l1.val
                l1 = l1.next
            y = 0
            if l2:
                y = l2.val
                l2 = l2.next
            x += y + carry
            carry = x // 10
            tail.next = ListNode(x % 10)
            tail = tail.next
        return head.next
sol = Solution()
l1 = ListNode(1, ListNode(9, ListNode(3)))
l2 = ListNode(4, ListNode(5, ListNode(6)))
l3 = ListNode(5, ListNode(4, ListNode(0, ListNode(1))))
myl3 = sol.addTwoNumbers(l1, l2)
print("correct:", l3, 'mine:', myl3)
assert l3 == myl3

l1 = ListNode(0)
l2 = ListNode(4, ListNode(5, ListNode(6)))
l3 = ListNode(4, ListNode(5, ListNode(6)))
assert l3 == sol.addTwoNumbers(l1, l2)

l1 = ListNode(0)
l2 = ListNode(0)
l3 = ListNode(0)
assert l3 == sol.addTwoNumbers(l1, l2)
