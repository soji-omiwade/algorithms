def flip(arr, k):
  lo = 0
  hi = k - 1
  while lo < hi:
    arr[lo], arr[hi] = arr[hi], arr[lo]
    lo += 1
    hi -= 1
  
'''
1 5 4 3 2

for each backidx = n - 1 .. 1
  find max idx, from 0 .. backidx
  flip(arr, maxidx + 1)
  flip(arr, backidx + 1)
  
'''
def pancake_sort(arr):
  n = len(arr)
  for backidx in range(n - 1, -1, -1): # 3
    maxidx = 0
    for idx in range(backidx + 1):
      if arr[idx] > arr[maxidx]:
        maxidx = idx
    flip(arr, maxidx + 1)
    flip(arr, backidx + 1)
  return arr
