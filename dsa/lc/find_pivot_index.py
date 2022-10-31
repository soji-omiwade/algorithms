class Solution:
    '''
    1,7,3,6,5,6
      ^

    idx = 0
    if idx >= n return -1
    sum all to right since leftmost idx is answer in multple solution case
    leftsum = 0
    rightsum = sumall - nums[idx]
    
    
    L: then check if both sums are equal. if so ans is idx. return it
    idx += 1
    if idx >= n return -1
    leftsum += nums[idx - 1]
    rightsum -= nums[idx]
    goto L
    '''
    def pivotIndex(self, nums: List[int]) -> int:
        idx, n = 0, len(nums)
        if idx >= n: 
            return -1
        # sum all to right since leftmost idx is answer in multple solution case
        leftsum = 0
        rightsum = sum(nums) - nums[idx]

        while leftsum != rightsum:
            # L: then check if both sums are equal. if so ans is idx. return it
            idx += 1
            if idx >= n:
                return -1
            leftsum += nums[idx - 1]
            rightsum -= nums[idx]
        return idx
