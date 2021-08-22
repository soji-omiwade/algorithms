'''
start ---- point-circle

relax; try to have fun!
   f2      f,s 
1 - 2 - 3 - 4
    |_______|
ans = 2


2nd example
1 - 2 - 3
'''
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def cycle_location(head: ListNode):
    fast = slow = head
    while slow and fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow is fast:
            break
            
    if not fast or not fast.next:
        return None
    print('slow', slow.val)
    # import sys
    # sys.exit()
    first = head
    second = slow
    while first is not second:
        first = first.next
        second = second.next
    return first       

four = ListNode(4)
head = ListNode(1, ListNode(2, ListNode(3, four)))
four.next = head.next
print(cycle_location(head).val) # 2
four.next = None
print(cycle_location(head)) # null


