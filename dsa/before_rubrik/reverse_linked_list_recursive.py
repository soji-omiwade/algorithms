'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
1<->2 <- 3, h -> null
def reverseList(curr)
    if not curr.next:
        head = curr
        return
    reverseList(curr.next)
    curr.next.next = curr
    curr.next = None
    return head
    
tail = head
head = call helper at head #
tail.next = null

T: O(n)
S: O(n)
'''
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return res
        