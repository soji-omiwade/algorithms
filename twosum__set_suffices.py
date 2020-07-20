from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = set([])
        for i in range(len(nums)):
            complements |= {target - nums[i]}
        res = []
        for i in range(len(nums)):
            if nums[i] in complements:
                res += [i]
        if len(res) == 2:
            return res
        for i in range(len(res)):
            if 2 * nums[res[i]] == target:
                res.pop(i)
                break
        return res
sol = Solution()
a = [9, 8, 2, 42, 77, 99, 1]; target = 11
assert sol.twoSum(a, target) in ([0, 2], [2, 0])
a = [9, 6, 8, 2, 42, 3, 77, 99, 1]; target = 12
assert sol.twoSum(a, target) in ([0, 5], [5, 0])
