'''
1st = O(n + m)
2nd = O(n lg m)

1st:
top = bot = 0
while top < n and bot < m
  if topel == botel
    output.append
  if topel < botel
    
'''
def binsearch(arr, key):
  #true if exists, topel, false otherwise
  lo, hi = 0, len(arr) - 1
  while lo <= hi:
    mid = (lo + hi) // 2
    if arr[mid] == key:
      return True
    if arr[mid] > key:
      hi = mid - 1
    else:
      lo = mid + 1
  return False

def find_duplicates(arr1, arr2):
  output = []
  for topel in arr1:
    if binsearch(arr2, topel):
      output.append(topel)
  return output

def linear_find_duplicates(arr1, arr2):
  top = bot = 0
  output = []
  n, m = len(arr1), len(arr2)
  while top < n and bot < m:
    topel, botel = arr1[top], arr2[bot]
    if topel == botel:
      output.append(topel)
    if topel < botel:
      top += 1
    else:
      bot += 1
  return output

arr1 = [1, 2, 3, 3, 5, 5, 5, 6, 7]
arr2 = [3, 6, 6, 6, 7, 8, 20]
print(find_duplicates(arr1, arr2)) # 3 6 7

arr1 = [4]
arr2 = [2]
print(find_duplicates(arr1, arr2)) #
