# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
relax

have fun

i/o

constraints

pseudocode

fill up both stacks
    
res = null
while top of both stacks are equal 
    res = pop both of them   
return res
'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def populate_stack(linkedlis):
            st = []
            while linkedlis:
                st.append(linkedlis)
                linkedlis = linkedlis.next
            return st
        
        sta = populate_stack(headA)
        stb = populate_stack(headB)
        
        res = None
        while sta and stb and sta[-1] == stb[-1]:
            res = sta.pop()
            stb.pop()
        return res