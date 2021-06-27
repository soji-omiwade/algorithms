'''
-5 1 2 2
4 4
'''
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightsum = sum(val for val in nums)
        leftsum = 0
        for idx, val in enumerate(nums):
            rightsum -= val
            if leftsum == rightsum:
                return idx
            leftsum += val
        return -1
        