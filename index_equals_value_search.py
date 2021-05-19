def index_equals_value_search(arr):
    '''
    res = -1
    while lo > hi
        if mid == arr[mid]
            done? no
            remember mid as the result, res
            hi = mid - 1
        else
            if mid > arr[mid]
                lo = mid + 1
            else
                hi = mid - 1
    return res       
    '''        
    res = -1
    lo = 0
    hi = len(arr)
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if mid == arr[mid]:
            res = mid
            hi = mid - 1
        else:
            if mid > arr[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
    return res          

assert index_equals_value_search([-8, -25, 2, 3, 28]) == 2
assert index_equals_value_search([-8, -25, 1, 3, 28]) == 3
assert index_equals_value_search([-8, -25, 12, 13, 28]) == -1