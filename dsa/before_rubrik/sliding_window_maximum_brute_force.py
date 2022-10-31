from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def max_in_place(a, start):
            res = a[start]
            for i in range(start, start + k):
                if a[i] > res:
                    res = a[i]
            return res
            
        n = len(nums)
        res = [0 for i in range(n-k+1)]
        for i in range(n-k+1):
            res[i] = max_in_place(nums, i)
        return res
maxwindow = Solution().maxSlidingWindow
assert maxwindow([4, 2, 3, 5], 2) == [4, 3, 5]
assert maxwindow([4, 2, 3, 5], 3) == [4, 5]
