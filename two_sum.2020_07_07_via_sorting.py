from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lo, hi = 0, len(nums) - 1
        sortednums = sorted(nums)
        while lo < hi:
            _sum = sortednums[lo] + sortednums[hi]
            if _sum == target:
                break
            if _sum > target:
                hi -= 1
            else:
                lo += 1
        res = []
        for i in range(len(nums)):
            if nums[i] in (sortednums[lo], sortednums[hi]):
                res.append(i)
        return res
        
assert Solution().twoSum([2,7,11,15], 9) == [0, 1]
assert Solution().twoSum([21,2,7,11,15, 21], 42) == [0, 5]
assert Solution().twoSum([2,7,11,4,15,-3], 8) == [2, 5]