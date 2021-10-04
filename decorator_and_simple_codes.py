'''
noon
no4on
f
<empty>
other
friday

left = 0
right = len(string) - 1
while left < right
    if string[left] != string[right]
        return false
    left += 1
    right -= 1
return true
'''
# def hello():
    
# hello()

strings = [
'noon'
,'no4on'
,"f"
,'other'
,""
]

import time

def add_timer(func, *args):
    starttime = time.time()
    val = func(*args)
    return time.time() - starttime, val

    
def pal(string):
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

timer_pal = add_timer(pal, "noon")
timer_pal(...)

# for string in strings:
    # print(pal(string))


arr = [4, 1, 2, 3, 5]
arr = [5, 4, 3, 2, 1]
arr = arr[::-1]
from typing import List
def bubblesort(arr: List[int]) -> None:
    for idx in range(len(arr)):
        for otheridx in range(len(arr) - idx - 1):
            if arr[otheridx] < arr[otheridx + 1]:
                arr[otheridx], arr[otheridx+1] = arr[otheridx+1], arr[otheridx]
bubblesort(arr)
print(arr)