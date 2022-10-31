from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(len(nums)-k):
            heapq.heappop(nums)
        return nums[0]
        
assert Solution().findKthLargest([3,2,1,5,6,4],2) == 5
assert Solution().findKthLargest([3,2,3,1,2,4,5,5,6],4) == 4
