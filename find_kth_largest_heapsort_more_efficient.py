from typing import List
from heapq import heappop,heappush
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq=[]
        for i in range(k):
            heappush(pq,nums[i])
        for i in range(k,len(nums)):
            heappush(pq,nums[i])
            heappop(pq)
        return pq[0]
        
from random import shuffle
a=[2*x for x in range(10)]
shuffle(a)
assert Solution().findKthLargest(a,3) == 14
a=[2*x for x in range(10)]
shuffle(a)
assert Solution().findKthLargest(a,1) == 18
a=[2*x for x in range(10)]
shuffle(a)
assert Solution().findKthLargest(a,len(a)) == 0
a=[1,1,1,1,1]
assert Solution().findKthLargest(a,len(a)) == 1
a=[1,1,1,1,1]
assert Solution().findKthLargest(a,3) == 1
a=[1,1,1,1,1]
assert Solution().findKthLargest(a,1) == 1
assert Solution().findKthLargest([3,2,1,5,6,4],2) == 5
assert Solution().findKthLargest([3,2,3,1,2,4,5,5,6],4) == 4
