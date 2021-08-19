'''
for each number at idx i, a[i]
    put that number at idx a[i] - 1 (and bring what is in a[i]-1, here to idx i)  so we have 
arr [1 2 3 4]
idx  0 1 2 3
    But stop if you cant
        - a[i] <= 0 or a[i] > len(a)
        
'''
from typing import List
def first_positive_number(arr: List[int]) -> int:
    for i in range(len(arr)):
        while arr[i] != i + 1 and 0 < arr[i] <= len(arr):
            arr[arr[i] - 1], arr[i], = arr[i], arr[arr[i] - 1]
    for i, val in enumerate(arr):
        if i + 1 != val:
            return i + 1
    else:
        return len(arr) + 1

arr = [2, 3, 4, -1, 48, 0]
#      i  aim1
print(first_positive_number(arr)) #1

arr = [2, 3, 4, 1, 48, 0]
print(first_positive_number(arr)) #5

arr = []
print(first_positive_number(arr)) #1
