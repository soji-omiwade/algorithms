class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        d = {}
        for i in range(len(nums)):
            d[(target-nums[i])] = i
            
        for i in range(len(nums)):
            x = nums[i]
            if x in d and d[x] != i:
                return [i, d[x]]

print(Solution().twoSum([2,7,11,15],9))