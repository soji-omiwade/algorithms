Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """1->2->3->4->5 ----> 54321"""
        try:
            self.top_head
        except:
            self.top_head = head
        if not head:
            return None
        if not head.next:
            return head
            
        res = self.reverseList(head.next)
        
        head.next.next = head
        if head is self.top_head:
            head.next = None
        return res
        
        
assert dump_list(Solution().reverseList(buildlist(mylist)))
    == dump_list(buildlist(reversed(mylist)))
