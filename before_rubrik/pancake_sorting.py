def flip(arr, k):
  for i in range(k//2):
    arr[i], arr[k-i-1] = arr[k-i-1], arr[i]

def find_maximum_element(arr, n):
  maxidx = 0
  for i in range(n):
    if arr[i] > arr[maxidx]:
      maxidx = i
  return maxidx

def pancake_sort(arr):
  n = len(arr)
  for i in range(n-1, 0, -1): # O(n)
    maxidx = find_maximum_element(arr, i+1) #find the max in window [0, i]
    flip(arr, maxidx + 1)
    flip(arr, i + 1)
  return arr

a = list('51432')
assert pancake_sort(a) == sorted(a)
a = list('12345')
assert pancake_sort(a) == sorted(a)
a = list('11111111')
assert pancake_sort(a) == sorted(a)

