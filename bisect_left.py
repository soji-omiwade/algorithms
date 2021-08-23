'''
breathe...and have fun!

2 3 7 7 7 8 9 
2 3 7 7
7 7
'''
def bisect(arr, x, lo, hi):
    ...
    
def bisect_left(arr, x, lo, hi):
    hi -= 1
    if arr[hi] < x:
        return hi + 1
    while lo < hi:
        mid = lo + (hi - lo) //2
        if arr[mid] < x:
            lo = mid + 1
        else: # >=
            hi = mid
    return lo # if it was found. how bout not!

arr = [2, 3, 7, 7, 7, 8, 9]    
x = 7
print(bisect_left(arr, x, 0, len(arr))) #2
x = 6
print(bisect_left(arr, x, 0, len(arr))) #2
x = 99
print(bisect_left(arr, x, 0, len(arr))) #7