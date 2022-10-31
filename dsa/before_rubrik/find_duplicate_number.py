from typing import List
'''
Input: nums = [1,3,4,2,2]
Output: 2
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # [1,3,4,2,2]
        for idx in range(len(nums)): #1, 3
            while nums[idx] != idx + 1: # 4 != 2
                if nums[idx] == nums[nums[idx] - 1]: #4 == 2
                    return nums[idx]
                val = nums[nums[idx] - 1] # 2 
                nums[nums[idx] - 1] = nums[idx] #   nums <-- 4
                nums[idx] = val     #
        raise Exception("shouldn't be here")

nums = [1,2,3,4,2]
nums = [1,2,3,4,2]        
print(Solution().findDuplicate(nums), nums) #2