from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        """
        complements = set([])
        for i in range(len(nums)):
            print(target - nums[i], nums[i])
            complements |= {target - nums[i]}
        res = []
        print(complements)
        for i in range(len(nums)):
            if nums[i] in complements:
                res += [i]
        if len(res) == 2:
            return res
        assert len(res) == 3
        print(res, "***")
        for i in range(len(res)):
            print(nums, res[i])
            if 2 * nums[res[i]] == target:
                res.pop(i)
                break
        return res
sol = Solution()
a = [9, 8, 2, 42, 77, 99, 1]; target = 11
assert sol.twoSum(a, target) in ([0, 2], [2, 0])
print("\n")
a = [9, 6, 8, 2, 42, 3, 77, 99, 1]; target = 12
print(sol.twoSum(a, target))
assert sol.twoSum(a, target) in ([0, 5], [5, 0])
