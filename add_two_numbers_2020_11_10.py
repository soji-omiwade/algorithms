# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def get_and_advance(ls):
            oldval = 0
            if ls:
                oldval = ls.val
                ls = ls.next
            return ls, oldval
            
        head = curr = ListNode()
        carry = 0
        while carry or l1 or l2:
            l1, l1oldval = get_and_advance(l1)
            l2, l2oldval = get_and_advance(l2)
            curr.next = ListNode((carry + l1oldval + l2oldval) % 10)
            carry = (carry + l1oldval + l2oldval) // 10
            curr = curr.nextx
        return head.next
        
l1 = ListNode(2, ListNode(8, ListNode(1)))
l2 = ListNode(7, ListNode(3, ListNode(3)))
l3 = Solution().addTwoNumbers(l1, l2)
one = l3.val
two = l3.next.val
three = l3.next.next.val
four = l3.next.next.next
assert one == 9 and two == 1 and three == 5 and four is None