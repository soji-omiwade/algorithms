'''
1, 3, 4, 2, 2
         lo,hi

mid = 3 => cnt == 4 > mid --> hi = 3
mid = 2 -> hi = 2
1 2 2 3 

mid = 1. count < 1 out of 3
n = len(nums) - 1
lo = 1
hi = n
while lo < hi
    mid = lo + (hi - lo) // 2
    count # of elems <= mid
    if count > mid
        hi = mid
    else
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1 # 4
        lo = min(nums)
        hi = max(nums)
        while lo < hi:
            '''
            1 1 1 3 4
            1 4 4 2 4
            (3) 4 4 4
            '''
            mid = lo + (hi - lo) // 2
            # of elems <= mid
            count = len(list(val for val in nums if val <= mid))
            if count > mid:
                hi = mid
            else: #count == mid
                lo = mid + 1
        return lo