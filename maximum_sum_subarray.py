'''
i = j = 0
cum = 0
while j < n
    cum += arr[j]
    if cum 
    j += 1
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = runningsum = float("-inf")
        for j in range(len(nums)):
            runningsum += nums[j]
            if nums[j] > runningsum:
                runningsum = nums[j]
            maxsum = max(maxsum, runningsum)
        return maxsum
