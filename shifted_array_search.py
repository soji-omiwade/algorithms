from typing import List
def shifted_array_search(arr: List[int], key: int):
    '''
    find start index sidx
        . divide array: lo, mid hi
        
        . if arr[lo] < arr[mid] < arr[hi] or lo = mid = hi: return lo
        . if arr[mid] > arr[hi]
            lo = mid + 1 
        . if arr[lo] > arr[mid]: it is here (and could be mid)
            hi = mid
    then use sidx and sidx + (n - 1) in a regular binary search
    '''
    n = len(arr)
    lo = 0
    hi = n - 1
    while True:
        mid = (lo + hi) // 2
        if (arr[lo] < arr[mid] < arr[hi] or lo == mid == hi or (lo == mid and arr[lo] < arr[hi])):
            sidx = lo
            break
        if arr[mid] > arr[hi]:
            lo = mid + 1
        elif arr[lo] > arr[mid]:
            hi = mid
        else:
            raise Exception("cant be here")
    lo = sidx
    hi = (sidx - 1) % n
    while True:
        if hi < lo: 
            hi += n
        mid = (lo + hi) // 2 % n
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            hi = mid - 1
        else:
            lo = mid + 1
    raise Exception("not found")
    
#[10, 11, 12, 3, 4, 5, 6, 7, 8, 9] [10, 11, 12, 3, 4, 5, 6, 7, 8, 9]
arr = [i for i in range(10)]
arr = [arr[i] + 10 for i in range(3)] + arr[3:]
assert (shifted_array_search(arr, 11) == 1)
assert (shifted_array_search(arr, 9) == 9)
assert (shifted_array_search(arr, 5) == 5)
