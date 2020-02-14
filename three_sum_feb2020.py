from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        done=set([])
        
        def two_sum(i,nums):
            foo=set([])
            target=-nums[i]
            d={}
            for j in range(i+1,len(nums)):
                d[target-nums[j]]=j
            for j in range(i+1,len(nums)):
                if nums[j] in d and d[nums[j]] != j:
                    x,y=nums[j],target-nums[j]
                    if x > y:
                        x,y=y,x
                    foo.add((-target,x,y))
            return foo
        
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if nums[i] not in done:
                res+=list(two_sum(i,nums))
                done.add(nums[i])
        return res
        
print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))