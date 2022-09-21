class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def helper(head, prev=None):
            '''
         nil < 1  2 > nil
         p  h   s
            '''
            if not head:
                return prev
            save = head.next
            head.next = prev
            return helper(save, head)

        return helper(head)
'''        
        if not head or not head.next:
            return head
        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return res
'''