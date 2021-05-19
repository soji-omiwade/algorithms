from typing import List
class Solution:
    def search(self, arr: List[int], key: int) -> int:
        n = len(arr)
        lo = 0
        hi = n - 1
        while arr[hi] < arr[lo]:
            mid = (lo + hi) // 2
            if arr[lo] > arr[mid]: # or lo == mid:
                hi = mid
            elif arr[mid] > arr[hi]:
                lo = mid + 1
            else:
                raise Exception("should not be here")
        hi = lo - 1
        if lo > hi:
            hi += n
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid % n] == key:
                return mid % n
            if arr[mid % n] > key:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1
# 0    1   2  3  4         
#[10, 11, 12, 3, 4, 5, 6, 7, 8, 9] [10, 11, 12, 3, 4, 5, 6, 7, 8, 9]
shifted_array_search = Solution().search
arr = [i for i in range(10)]
arr = [arr[i] + 10 for i in range(3)] + arr[3:]
assert (shifted_array_search(arr, 11) == 1)
assert (shifted_array_search(arr, 9) == 9)
assert (shifted_array_search(arr, 5) == 5)
arr = [4,5,6,7,0,1,2]
key = 3
assert (shifted_array_search(arr, key) == -1)
arr = [4,5,6,7,0,1,2]
key = 4
assert (shifted_array_search(arr, key) == 0)
arr = [4,5,6,7,0,1,2]
key = 7
assert (shifted_array_search(arr, key) == 3)
