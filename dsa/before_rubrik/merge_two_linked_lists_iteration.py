class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next
        
    def __str__(self):
        v=self
        s=[]
        while v is not None:
            s.append(str(v.val))
            v=v.next
        return "".join(s)
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        prehead=ListNode(-1)
        prev=prehead
        while l2 is not None and l1 is not None:
            if l1.val <= l2.val:
                prev.next=l1
                l1 = l1.next
            else: 
                prev.next=l2
                l2=l2.next
            prev=prev.next
        if l1 is None:
            prev.next=l2
        else:
            prev.next=l1
        
        return prehead.next
      
l1=ListNode(2,ListNode(4,ListNode(6)))      
l2=ListNode(1,ListNode(3,ListNode(5)))      
print(Solution().mergeTwoLists(l1,l2))