from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        res = []
        if not nums:
            return res
        q = deque()
        for i in range(len(nums)):
            if q and q[0] == i - k:
                q.popleft()
            while q and nums[q[-1]] < nums[i]:
                q.pop()            
            q.append(i)
            if i >= k - 1:
                res.append(nums[q[0]])
        return res