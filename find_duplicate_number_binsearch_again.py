'''
find duplicate number
rhici
relax & have fun
i/o
[2 1 3 3 4 5]
1 8 --> 4 --> count how many

constraints
implement
complexity
O(n * n)
maxval
'''
from typing import List
def duplicate_number(arr: List[int]):
    lo, hi = min(arr), max(arr)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        count = 0
        for elem in arr:
            if elem <= mid:
                count += 1
        if count == mid:
            lo = mid + 1
        elif count > mid:
            hi = mid
    return arr[lo]
    
arr = [2, 1, 3, 3, 4, 5]
print(duplicate_number(arr)) #3
    