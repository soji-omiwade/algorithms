# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def next_(lis: ListNode):
            if lis:
                return lis.next
            return None
        res = curr = ListNode(None)
        carry = 0
        while l1 or l2 or carry:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            sum_ = l1val + l2val + carry
            carry = sum_ // 10
            curr.next = ListNode(sum_ % 10)
            curr = curr.next
            l1 = next_(l1)
            l2 = next_(l2)
        return res.next
        
lone = ListNode(2, ListNode(4, ListNode(3)))
ltwo = ListNode(5, ListNode(6, ListNode(4)))
lres = Solution().addTwoNumbers(lone, ltwo)
ans = [7, 0, 8]
count = 0
while lres:
    print(ans[count], lres.val)
    assert ans[count] == lres.val
    count += 1
    lres = lres.next
    
lone = ListNode(2, ListNode(4, ListNode(8, ListNode(8))))
ltwo = ListNode(5, ListNode(6, ListNode(4)))
lres = Solution().addTwoNumbers(lone, ltwo)
ans = [7, 0, 3, 9]
count = 0
while lres:
    print(ans[count], lres.val)
    assert ans[count] == lres.val
    count += 1
    lres = lres.next