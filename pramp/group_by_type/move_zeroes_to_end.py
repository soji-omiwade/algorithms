'''
time O(n^2)
space O(1)
"shift elem"

time O(n)
space O(n)
new array

time O(n)
space O(1)
move elem all the way
'''
def moveZerosToEnd(arr):
  """
  @param arr: int[]
  @return: int[]
  """
  lo = hi = 0
  for hi in range(len(arr)):
    if arr[hi] != 0:
      arr[lo] = arr[hi]
      if lo != hi:
        arr[hi] = 0
      lo += 1
  return arr
  
arr = [1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]
print(moveZerosToEnd(arr))
