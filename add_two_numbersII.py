# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def print(self):
        v = self
        while v:
            print(v.val, end="-->")
            v = v.next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        v = l1
        foo = 1
        x = 0
        while v:
            x += v.val * foo
            foo *= 10
            v = v.next
            
        v = l2
        foo = 1
        y = 0
        while v:
            y += v.val * foo
            foo *= 10
            v = v.next
        res_int = x+y
        
        #807 => 7-0-8
        res = None
        while True:
            val = res_int % 10
            res_int //= 10
            v = ListNode(val)
            if not res:
                #first time through only
                res = last = v
            else: 
                last.next = v
                last = v
            if res_int == 0:
                break
        return res

Solution().addTwoNumbers(ListNode(243), ListNode(564)).print()