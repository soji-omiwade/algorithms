# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry=0
        head=tail=None
        while l1 is not None or l2 is not None or carry>0:
            x=0 if l1 is None else l1.val
            y=0 if l2 is None else l2.val
            v=ListNode((x+y+carry)%10)
            if head is None and tail is None:
                head=tail=v
            else:
                tail.next=v
                tail=v
            carry=(x+y+carry)//10
            
            l1=None if l1 is None else l1.next
            l2=None if l2 is None else l2.next
        return head