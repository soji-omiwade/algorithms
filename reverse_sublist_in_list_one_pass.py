'''
i/o
1 2 3 4 5
h   l r
ans = 
1 2 4 3 5
h
constraints
n > 0
0 < l, r <= n
diagram
    walk to node l
    hp, tp = call reverse(node-l, r)
    attach prev to node l + (hp, tp)
    note: reverse

pseudocode
curr = head
for i in range(left - 1):
    prev, curr = curr, curr.next

oldnoderightnext = reverse_list(curr)

attach three!
prev.next = oldnoderight
curr.next = oldnoderightnext

1 < 2 < 3 > ...
l       r
       p,c
       
1
l,r

function reverse_list(curr)
    prev, curr = curr, curr.next
    for i in range(right - left):
        curr_next = curr.next
        curr.next = prev
        prev, curr = curr, curr_next
    return curr
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        def reverse_list(curr: ListNode) -> Tuple[ListNode, ListNode]:
            prev, curr = curr, curr.next
            for i in range(right - left):
                curr_next = curr.next
                curr.next = prev
                prev, curr = curr, curr_next
            return prev, curr
        
        dummy = ListNode(None, head)
        prev, curr = dummy, head
        for i in range(left - 1):
            prev, curr = curr, curr.next
        #curr is left node
        oldnoderight, oldnoderightnext = reverse_list(curr)
        #attach three!
        prev.next = oldnoderight
        curr.next = oldnoderightnext
        
        return dummy.next
            
'''
        0 > 1 < 2 < 3 > ...
            l       r
        p   c

        1
        l,r
'''