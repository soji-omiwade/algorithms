from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        accumulated_product=1
        res=[1]
        n=len(nums)
        for i in range(1,n):
            res.append(accumulated_product*nums[i-1])
            accumulated_product*=nums[i-1]
        accumulated_product=nums[n-1]
        for i in range(n-2,-1,-1):
            res[i]*=accumulated_product
            accumulated_product*=nums[i]
        return res

nums,res=[1,2,3,4],[24,12,8,6]
assert Solution().productExceptSelf(nums)==res
nums,res=[8,2,1,3,6],[36,144,288,96,48]
assert Solution().productExceptSelf(nums)==res
nums,res=[8,2],[2,8]
assert Solution().productExceptSelf(nums)==res
            
        
            