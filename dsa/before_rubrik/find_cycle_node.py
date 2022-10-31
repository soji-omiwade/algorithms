'''
find the node having a cycle
time: 12:45 -- ...
    setup: -- 1:08 = 23 mins!
    algorithm -- ...
    implementation -- 1:27 = total 42 mins! good job!!
    explanation of approach: ---1:35 total 50mins
'''
import sys
class ListNode:
    def __init__(self, val: str, next: 'ListNode' = None):
        self.val = val
        self.next = next

'''
a b c d e f  --> c
  
b c d e f 
c e c e c
      ^
'''        
def listgen(head: 'ListNode'):
    while head:
        yield head
        head = head.next

def findmeetpoint(head):
    slow = fast = head
    slow = slow.next
    fast = slow.next
    while slow is not fast:
        slow = slow.next
        fast = fast.next.next
    return slow
    
def findcyclenode(head: ListNode) -> ListNode:
    meetpoint = findmeetpoint(head)
    curr1, curr2 = head, meetpoint
    while curr1 is not curr2:
        curr1 = curr1.next
        curr2 = curr2.next
    return curr1

four = ListNode('4',
    )
f = ListNode('f',
    ListNode('3',
    four))
head = ListNode('1', 
    ListNode('2',
    ListNode('a', 
    ListNode('b',
    ListNode('c',
    ListNode('d', 
    ListNode('e',
    f)))))))
four.next = head.next.next.next.next
print(four.next.val) #c

assert head.next.val == '2'    
assert head.val == '1'    
# for node in listgen(head):
    # print(f"{node.val}", end=", ")
# print()

node = findcyclenode(head)
print(node.val) #c