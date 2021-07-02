class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def threesum(target):
            def twosum(target):
                lo, hi = cidx + 1, len(nums) - 1
                while lo < hi:
                    if nums[lo] + nums[hi] == target:
                        if res[-1] != [d, c, nums[lo], nums[hi]]:
                            res.append([d, c, nums[lo], nums[hi]])
                        lo += 1
                        hi -= 1
                    elif nums[lo] + nums[hi] > target:
                            hi -= 1
                    else:
                        lo += 1
            lastc = None
            for cidx, c in enumerate(nums[didx + 1:], didx + 1):
                if c != lastc:
                    twosum(target - c)
                lastc = c
            
        res = [None]
        nums = sorted(nums)
        lastd = None
        for didx, d in enumerate(nums):
            if d != lastd:
                threesum(target - d)
            lastd = d
        return res[1:]