from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        from math import inf
        mn_sum=inf
        res=[]
        for i in range(len(nums)):
            lo,hi=i+1,len(nums)-1
            while lo < hi:
                if abs(nums[lo]+nums[hi]+nums[i]-target)<abs(mn_sum-target):
                    mn_sum=nums[lo]+nums[hi]+nums[i]
                #now do i go left or right?
                if nums[lo]+nums[hi]+nums[i] == target:
                    return mn_sum
                if nums[lo]+nums[hi]+nums[i] < target:
                    lo+=1
                else:
                    hi-=1
        
        return mn_sum
print(Solution().threeSumClosest([-1,2,1,-4],1))