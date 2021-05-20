from typing import List
class Solution:
    def even_more_elegant_pivotIndex(self, arr: List[int]) -> int:
        left = 0
        right = sum(arr)
        for idx, num in enumerate(arr):
            right -= num
            if left == right:
                return idx
            left += num
        return -1
        
    def elegant_pivotIndex(self, arr: List[int]) -> int:
        '''
        same as method below without using iterator next method
        '''
        from itertools import chain
        left = 0
        right = sum(val for val in arr)
        prev = 0
        for idx, curr in enumerate(arr):
            left += prev
            right -= curr
            if left == right:
                return idx 
            prev = curr
        return -1
        
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
        for idx in range(len(arr)):
            curr = next(arr_iter)
            left += prev
            right -= curr
            prev = curr
            if left == right:
                return idx
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

arr = [1, 7, 3, 6, 5, 6]
res = 3        
Solution().elegant_pivotIndex(arr) == res
arr = []
res = -1        
Solution().elegant_pivotIndex(arr) == res
arr = [1, 7, 3, 6, 6, 6]
res = -1
Solution().elegant_pivotIndex(arr) == res
arr = [11, -2, 1, 1]
res = 0
Solution().elegant_pivotIndex(arr) == res

arr = [1, 7, 3, 6, 5, 6]
res = 3        
Solution().even_more_elegant_pivotIndex(arr) == res
arr = []
res = -1        
Solution().even_more_elegant_pivotIndex(arr) == res
arr = [1, 7, 3, 6, 6, 6]
res = -1
Solution().even_more_elegant_pivotIndex(arr) == res
arr = [11, -2, 1, 1]
res = 0
Solution().even_more_elegant_pivotIndex(arr) == res
