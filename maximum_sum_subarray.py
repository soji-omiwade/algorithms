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
        runningsum = nums[0]
        maxsum = runningsum
        i = 0
        n = len(nums)
        for j in range(1, n):
            runningsum += nums[j]
            if nums[j] > runningsum:
                runningsum = nums[j]
                i = j
            maxsum = max(maxsum, runningsum)
        return maxsum
        