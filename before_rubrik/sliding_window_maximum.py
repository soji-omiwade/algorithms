from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        if not nums:
            return res
        q = deque()
        for i in range(k):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
        res.append(nums[q[0]])
        for i in range(k, len(nums)):
            if q[0] == i - k:
                q.popleft()
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            res.append(nums[q[0]])
        return res
        
func = Solution().maxSlidingWindow
assert func([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
assert func([i for i in range(10)], 4) == [i for i in range(3,10)]
assert func([i for i in range(10,0,-1)], 4) == [i for i in range(10,3,-1)]
        