from typing import List 
def move_neg_numbs_to_end(arr: List[int]):
    lo = 0
    for hi in range(len(arr)):
        if arr[hi] < 0:
            arr[lo], arr[hi] = arr[hi], arr[lo]
            lo += 1
    return arr, lo


arr = [2, -3, -5, -2, 1, -4, 42]
print(move_neg_numbs_to_end(arr)) # 4

arr = [2, -3, 1, -4]
print(move_neg_numbs_to_end(arr)) # 2

arr = [2, 3, 1, 4]
print(move_neg_numbs_to_end(arr)) # 0

arr = [-2, -3, -1, -4]
print(move_neg_numbs_to_end(arr)) # 4

arr = []
print(move_neg_numbs_to_end(arr)) # 0

