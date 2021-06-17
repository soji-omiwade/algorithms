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
                    ansleft = nums[left]
                    ansright = nums[right]
                    result.append([nums[left], nums[right], nums[farleft]])
                    while left < right and nums[left] == ansleft: 
                        left += 1
                    while right > left and nums[right] == ansright:
                        right -= 1
                elif nums[farleft] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
            ansfarleft = nums[farleft]
            while farleft < left and nums[farleft] == ansfarleft:
                farleft += 1
            # 3 of them must be moved to avoid duplicates
        return result
                
            