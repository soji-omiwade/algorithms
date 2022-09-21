'''
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

---------------
run through first element of all list and put in heap such that heap element = (heapval, counter, listnode) ---> [1,1,2]
while heap has elements:
    extract heap min element
    adjust result accordingly with that element
    if there is a next on the corresponding list of extracted element
        put next of listnode(of elemnt) in heap
T: O(k) + [lg k  *  m] = k +  m lg k
        

[...]
...
[...]
[...]

10 --> 5 5 -> 2 3 -> 

2 ---> m
...
k/4---> m
k/2 --> m
O(m * lg k)

return mergeklists(lists, 0, k - 1)

1->x
2->x
1.next = 2
1->2
1->2->x
5
function merge2lists(lis1, lis2):
    if lis1 or lis2 is None:
        return lis1 or lis2
    #both are not None
    if lis1.val < lis2.val:
        return lis1 + merge2lists(lis1.next, lis2)  --->  lis1.next = merge2lists...
    return lis2 + merge2lists(lis1, lis2.next)

function mergeklists(lists, start, end):
    if start == end:
        return lists[start]
    if start == end - 1:
        return merge2lists(lists[start], lists[end])
    #start < end - 1
    mid = (start + end) // 2
    return merge2lists(mergeklists(lists, start, mid), mergeklists(lists, mid + 1, end))
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge2lists(lis1: ListNode, lis2: ListNode):
            if not lis1 or not lis2:
                return lis1 or lis2
            #both are not None
            if lis1.val < lis2.val:
                lis1.next = merge2lists(lis1.next, lis2)
                return lis1
            lis2.next = merge2lists(lis1, lis2.next)
            return lis2

        def helper(start, end):
            if start == end:
                return lists[start]
            if end - start == 1:
                return merge2lists(lists[start], lists[end])
            #start < end - 1
            mid = (start + end) // 2
            return merge2lists(helper(start, mid), helper(mid + 1, end))
    
        if not lists:
            return None
        return helper(0, len(lists) - 1)