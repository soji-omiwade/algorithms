'''
1 2 3 
3 2 1
iterative:
if not head or not head.next
    return head   
#number of nodes > 1
p <- 1 <- 2    nil
f    t    s
prehead = Node(None, head)
from, to = prehead, head
while to
    save = to.next
    to.next = fromnode
    to = save
    from = to
head = fromnode
#tail is head
head.next = null
T: O(n)
S: O(1)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        fromnode = None
        while head:
            save = head.next
            head.next = fromnode
            fromnode, head = head, save
        return fromnode
