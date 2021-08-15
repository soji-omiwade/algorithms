# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
a 1 2 3 4 5 6
  ans intersect
slow 1 2 3 4 5 6 1
fast 2 4 6 2 4 6
 
a b 1 2 3 4 5 6
    ans     intersect
slow = b 1 2 3 4 5 6 1
fast = 1 3 5 1 3 5


  
fast c 1 3 5 1 3 5 1 3 5
slow b c d 1 2 3 4 5 6 1
               *        
               
3 2 0 4
slow 2 0 4 3
fast 0 3 0 3

number

1 3 
'''
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head 
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                start  = head
                while start is not slow:
                    start = start.next
                    slow = slow.next
                return slow
        return None

# 1 2 3  => ans = null
#   f s                
head = ListNode(1)
two = ListNode(2)
three = ListNode(3)
head.next = two
two.next = three
print(Solution().detectCycle(head)) # null


# 1 2 3 -> 1  => ans = 1
three.next = head
print(Solution().detectCycle(head).val) # 1

# -2 -1 1 2 3 -> -2  => ans = -2
negone = ListNode(-1)
negtwo = ListNode(-2)
negtwo.next = negone
negone.next = head
three.next = negtwo
print(Solution().detectCycle(negtwo).val) # -2


# -2 -1 1 2 3 -> 1  => ans = 1
three.next = head
print(Solution().detectCycle(negtwo).val) # 1

# import sys
# sys.exit()


