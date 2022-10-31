# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr=res=ListNode(0)
        carry=0
        while carry>0 or l1 or l2:
            x=y=0
            if l1:
                x=l1.val
                l1=l1.next
            if l2:
                y=l2.val
                l2=l2.next
            curr.next=ListNode((x+y+carry)%10)
            carry=(x+y+carry)//10
            curr=curr.next
        return res.next