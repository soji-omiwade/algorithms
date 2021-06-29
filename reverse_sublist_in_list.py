'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

prevleft, nextright
reverse(leftnode, rightnode)
prevleft.next = rightnode
leftnode.next = nextright

recursive: space: O(n)
go iterative
def reverse(head, tail)
    #when done head.next = None for example
    if head is tail return 
    p > 1 > 2 > 3 > null
    from = pre
    to = head
    while to
        save = to.next
        to.next = from
        from, to = to, save
    return
    1 > 2 > 3
    l       r
1 > 2 > 3 > 4 > nil
l,h     r   nr
pl = nil
left/right: 1 and 3

3 > 2 > 1 > 4
h
'''
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:            
        def reverse(head, tail):
            tailnext = tail.next
            if head is tail:
                return 
            #p > 1 > 2 > 3 > null
            fromnode, to = head, head.next
            while to is not tailnext:
                save = to.next
                to.next = fromnode
                fromnode, to = to, save
            return
                
        leftnode = head #1
        count = 1
        prevleft = None
        while count < left:
            prevleft = leftnode
            leftnode = leftnode.next
            count += 1
        rightnode = leftnode
        while count < right:
            rightnode = rightnode.next 
            count += 1
        nextright = rightnode.next #null
        reverse(leftnode, rightnode)
        if prevleft:
            prevleft.next = rightnode
        else:
            head = rightnode
        leftnode.next = nextright
        return head
'''
1 > 2 > 3 > 4 > nil
l,h     r   nr
pl = nil
left/right: 1 and 3

3 > 2 > 1 > 4
'''    