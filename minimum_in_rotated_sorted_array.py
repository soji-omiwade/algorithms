from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        #time 5:14
        lo = 0
        hi = len(nums) - 1
        while nums[lo] > nums[hi]:
            mid = (lo + hi) // 2 # lo + (hi - lo) // 2
            if nums[lo] > nums[mid]:
                hi = mid
            elif nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                raise Exception("cannot be here")
        return nums[lo]
        
arr = [22, 11]
findmin = Solution().findMin
assert findmin(arr) == 11
arr = [22, 27, 4, 11]
findmin = Solution().findMin
assert findmin(arr) == 4
