from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n=len(nums)
        for i in range(n-k+1): #at this point i, nums[:i] is sorted
            jm = i
            for j in range(i,n):
                if nums[j] < nums[jm]:
                    jm = j
            nums[i],nums[jm]=nums[jm],nums[i]
        return nums[n-k]
assert Solution().findKthLargest([3,2,1,5,6,4],2) == 5
assert Solution().findKthLargest([3,2,3,1,2,4,5,5,6],4) == 4
