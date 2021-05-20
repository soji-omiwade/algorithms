from typing import List
class Solution:
def pivotIndex(self, arr: List[int]) -> int:
    '''
    ...x...
    sumleft = 0
    sumright = sum arr minus arr[0]
    iterate, [[0] arr] from i = 1 to n-1:
        sumleft += arr[i - 1]
        sumright -= arr[i]
        if sumleft == sumright:
            return i
    return -1
    '''
    from itertools import chain
    sumleft = 0
    sumright = sum(val for val in arr)
    parr = chain([0], arr)
    prev_parr = next(parr)
    for ridx in range(len(arr)):
        curr_parr = next(parr)
        sumleft += prev_parr
        sumright -= curr_parr
        prev_parr = curr_parr
        if sumleft == sumright:
            return ridx
    return -1
        
arr = [1, 7, 3, 6, 5, 6]
res = 3        
Solution().pivotIndex(arr) == res
arr = []
res = -1        
Solution().pivotIndex(arr) == res
arr = [1, 7, 3, 6, 6, 6]
res = -1
Solution().pivotIndex(arr) == res
arr = [11, -2, 1, 1]
res = 0
Solution().pivotIndex(arr) == res

