'''
0 1 2
1 3 0

temp 1

'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] != i and nums[i] < len(nums):
                temp = nums[i] # 1
                nums[i] = nums[temp] #
                nums[temp] = temp # 
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)
        
'''
0 1 2 3 

3 0 1 
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xorall = len(nums)
        for i in range(len(nums)):
            xorall ^= i
            xorall ^= nums[i]
        return xorall
                