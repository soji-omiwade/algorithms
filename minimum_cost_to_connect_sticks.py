from typing import List
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        from heapq import heappop,heappush,heapify
        heapify(sticks)
        cost=0
        while len(sticks)>1:
            mn=heappop(sticks)
            mn2=heappop(sticks)
            heappush(sticks,mn+mn2)
            cost+=mn+mn2
        return cost
print(Solution().connectSticks([2,4,3]))
print(Solution().connectSticks([1,3,8,5]))