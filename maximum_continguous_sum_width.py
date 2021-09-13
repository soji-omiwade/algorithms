'''
[2, 8, 3, 5, 1], 
4
'''
from typing import List
def maxsumwindow(arr: List[int], width: int) -> int:
    n = len(arr)
    res = sum_ = sum(arr[idx] for idx in range(width))
    for lo in range(1, n - width + 1):
        hi = lo + width - 1
        sum_ -= arr[lo - 1]
        sum_ += arr[hi]
        if sum_ > res:
            res = sum_
    return res
arr = [2, 8, 3, 5, 1] 
width = 3
print(maxsumwindow(arr, width))