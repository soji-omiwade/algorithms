from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        from math import inf
        min_width=inf
        for i in range(len(nums)):            
            def closest_three_sum_i(i,nums,target):
                """pass target so we return only the min three sum of all i three sums"""
                mn=inf
                d={}
                tst=nums[i]
                for j in range(i+1,len(nums)):
                    d[tst-nums[j]]=j
                for j in range(i+1,len(nums)):
                    if nums[j] in d and j!=d[nums[j]]:
                        if abs(target-2*tst)<abs(target-mn):
                            mn=target-2*tst
                return mn
            min_three_sum_i=closest_three_sum_i(i,nums,target)
            min_width_i=abs(min_three_sum_i-target)
            if min_width_i < min_width:
                min_width=min_width_i
                min_three_sum=min_three_sum_i                
        return min_three_sum
        
print(Solution().threeSumClosest([-1,2,1,-4],1))