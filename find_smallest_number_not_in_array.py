def get_different_number(arr):
  '''
  [1,0,3,4,5]
  arrmine = sorted(arr)
  for idx, val in enumerate(arrmine):
    if idx != val:
      return idx
  return len(arr)
  '''
  for idx in range(len(arr)):
    while idx != arr[idx] and arr[idx] < len(arr):
      arr_idx = arr[idx]
      arr[idx], arr[arr_idx] = arr[arr_idx], arr[idx]
  for idx in range(len(arr)):
    if arr[idx] != idx:
      return idx
  return len(arr)

'''
0 1 4 3 5
2 < 4 < 5 ? yes
arr[2], arr[4] = arr[4], arr[2]
arr = [0,1,5,2,4]
print(arr)
assert get_different_number(arr) == 3
'''
