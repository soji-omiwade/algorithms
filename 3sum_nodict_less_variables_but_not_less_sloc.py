class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        farleft = 0
        result = []
        while farleft < len(nums):
            left = farleft + 1
            right = len(nums) - 1
            while left < right:
                if nums[farleft] + nums[left] + nums[right] == 0:
                    result.append([nums[left], nums[right], nums[farleft]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]: 
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[farleft] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
            farleft += 1
            while farleft < len(nums) and nums[farleft] == nums[farleft - 1]:
                farleft += 1
            # 3 of them must be moved to avoid duplicates
        return result