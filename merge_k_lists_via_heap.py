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
        

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
from itertools import count
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        '''
            run through first element of all list and put in heap such that heap element = (heapval, counter, listnode) ---> [1,1,2]
            while heap has elements:
                extract heap min element
                adjust result accordingly with that element
                if there is a next on the corresponding list of extracted element
                    put next of listnode(of elemnt) in heap    
        '''
        #[1->3, 2, None] --> [3, null, null]
        lisnodeheap = []
        counter = count()
        for idx, lishead in enumerate(lists):
            if lishead:
                lisnodeheap.append((lishead.val, next(counter), lishead))
                lists[idx] = lishead.next
        heapq.heapify(lisnodeheap)   
        curr = result = ListNode(None)
        while lisnodeheap: # 3
            element = heapq.heappop(lisnodeheap) #2
            node = element[-1]
            curr.next = node  #
            curr = curr.next
            if node.next:
                heapq.heappush(lisnodeheap, (node.next.val, next(counter), node.next))
        # curr.next = None
        return result.next # 1->2