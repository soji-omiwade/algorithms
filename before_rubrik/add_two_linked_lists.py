# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __str__(self):
        v=self
        s=""
        while v is not None:
            s+=str(v.val)
            v=v.next
        return s

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        val=0
        head=tail=None
        while l1 is not None or l2 is not None or val>0:
            if l1 is not None:
                val+=l1.val
                l1=l1.next
            if l2 is not None:
                val+=l2.val
                l2=l2.next               
            v=ListNode(val%10)
            
            if head is tail is None:
                head=tail=v
            else:
                tail.next=v
                tail=v
                
            val//=10
        return head
        
l1=ListNode(2,ListNode(4))
l2=ListNode(1,ListNode(3))
print(Solution().addTwoNumbers(l1,l2))