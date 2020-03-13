from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)):
            res ^= nums[i] ^ i
        return res ^ len(nums)

assert Solution().missingNumber([3,0,1]) == 2
assert Solution().missingNumber([9,6,4,2,3,5,7,0,1]) == 8
