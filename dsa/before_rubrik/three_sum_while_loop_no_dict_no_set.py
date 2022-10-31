from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res=[]
        for i in range(len(nums)):
            if i ==0 or (nums[i] != nums[i-1]):
                lo,hi=i+1,len(nums)-1
                while lo < hi:
                    if nums[lo]+nums[hi]+nums[i]==0:
                        res.append([nums[lo],nums[hi],nums[i]])
                        while lo<hi and nums[lo] == nums[lo+1]:
                            lo+=1
                        lo+=1
                        while lo<hi and nums[hi]==nums[hi-1]:
                            hi-=1
                        hi-=1
                    elif nums[lo]+nums[hi]+nums[i] < 0:
                        lo+=1
                    else: 
                        hi-=1
        return res
        
print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))