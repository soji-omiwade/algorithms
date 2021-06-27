'''
start: 1:29pm
end: 1:40pm
nums
2 ways: 
1st way: 
-sort it
-and then use 2 pointers from opposite sides to find the twosum hitting target
-complexity: O(n lg n). S: O(n). timsort 
2nd way: 
run trhough the nums, if target - val is in lookup. return val and target - val
T: O(n). S: O(n)
constraints:

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for idx, val in enumerate(nums):
            if target - val in lookup:
                return idx, lookup[target - val]
            lookup[val] = idx
        