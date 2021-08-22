'''
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next
'''
RHICI

Relax

Have fun

I/o
...

Clarify/constraints
...


Implement
diagram
0 - 1 - a - b - c 
            /
       x - y


@4 curra = 0
@4 currb = c
@6 currb = y
@6 curra = a
'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curra, currb = headA, headB
        while curra is not currb:
            if not curra:
                curra = headB
            else:
                curra = curra.next
            currb = currb.next if currb else headA
        return curra

ListNode(0, ListNode(1, ListNode("a")))        

            