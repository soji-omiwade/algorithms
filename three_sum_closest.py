from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        from math import inf
        mn=inf
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if abs(nums[i]+nums[j]+nums[k]-target) < abs(mn-target):
                        mn=nums[i]+nums[j]+nums[k]
        return mn
print(Solution().threeSumClosest([-1,2,1,-4],1))