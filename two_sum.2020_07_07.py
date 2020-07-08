from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        brosloc = {}
        n = len(nums)
        for i in range(n):
            brosloc[target - nums[i]] = i
        for i in range(n):
            if nums[i] in brosloc and brosloc[nums[i]] != i:
                return [i, brosloc[nums[i]]]
                
assert Solution().twoSum([2,7,11,15], 9) == [0, 1]
assert Solution().twoSum([21,2,7,11,15, 21], 42) == [0, 5]
assert Solution().twoSum([2,7,11,4,15,-3], 8) == [2, 5]