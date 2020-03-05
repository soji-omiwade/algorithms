class ListNode:
    def __init__(self, x,next=None):
        self.val = x
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        if l1 and l2:
            if l1.val > l2.val:
                l1,l2=l2,l1
            l1.next=self.mergeTwoLists(l1.next,l2)
            return l1
        if l2:
            return l2
        if l1:
            return l1
        

def equals(l1,l2):
    while l1 and l2:
        if l1.val!=l2.val:
            return False
        l1,l2=l1.next,l2.next
    if l1 or l2:
        return False
    return True
l1=ListNode(2,ListNode(4,ListNode(6)))
l2=ListNode(1,ListNode(3,ListNode(5)))
l3=ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6))))))
assert equals(l1,l1)
assert equals(l2,l2)
assert equals(l3,l3)
assert equals(Solution().mergeTwoLists(l1,l2),l3)


