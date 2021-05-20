from typing import List
class Solution:
def pivotIndex(self, arr: List[int]) -> int:
    '''
    ...x...
    left = 0
    right = sum arr minus arr[0]
    iterate, [[0] arr] from i = 1 to n-1:
        left += arr[i - 1]
        right -= arr[i]
        if left == right:
            return i
    return -1
    '''
    from itertools import chain
    left = 0
    right = sum(val for val in arr)
    arr_iter = chain([0], arr)
    prev = next(arr_iter)
    for ridx in range(len(arr)):
        curr = next(arr_iter)
        left += prev
        right -= curr
        prev = curr
        if left == right:
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

