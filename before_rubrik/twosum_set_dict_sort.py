from typing import List
class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
        # """
        # O(n) time algorithm to find the indexes of a two sum pair
        # """
        # comps = set()
        # locs = {}
        # for i in range(len(nums)):
            # if target - nums[i] in comps:
                # return [i, locs[target - nums[i]]]
            # comps.add(nums[i])
            # locs[nums[i]] = i
        # raise Exception("no two sum found")

    # def twoSum(self, nums: List[int], target: int) -> List[int]:
        # """
        # O(n) time algorithm to find the indexes of a two sum pair
        # """
        # comp_to_loc = {}
        # for i in range(len(nums)):
            # if target - nums[i] in comp_to_loc:
                # return [i, comp_to_loc[target - nums[i]]]
            # comp_to_loc[nums[i]] = i
        # raise Exception("no two sum found")
        
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #O(n lg n) time
        snums = sorted((nums[i],i) for i in range(len(nums)))
        lo, hi = 0, len(snums)-1
        while True:
            if snums[lo][0] + snums[hi][0] == target: return [snums[lo][1], snums[hi][1]]
            elif snums[lo][0] + snums[hi][0] < target: lo += 1
            else: hi -= 1
        raise Exception("no two sum found")

twosum = Solution().twoSum
assert twosum([2,4, 6, 6, 9, 5, 42], 9) in ([1,5], [5,1])
assert twosum([420, 2, 4, 3 ,9, 6, 42], 8) in ([1,5], [5,1])
assert twosum([420, 4, 8, 3 ,9, 4, 42], 8) in ([1,5], [5,1])

