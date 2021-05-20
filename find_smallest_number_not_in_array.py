def get_different_number_via_set(arr):
    '''
    this method isnt as sophisticated as the one below
    and it has O(n) space.
    but it is easier to understand
    '''
    set_arr = set(arr)
    for i in range(len(arr)):
        if i not in set_arr:
            return i
    return len(arr)
        
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

arr = [0, 1, 2, 3, 4]
res = 5
assert get_different_number(arr) == res
arr = [1, 0, 5, 58, 4]
res = 2
assert get_different_number(arr) == res


arr = [0, 1, 2, 3, 4]
res = 5
assert get_different_number_via_set(arr) == res
arr = [1, 0, 5, 58, 4]
res = 2
assert get_different_number_via_set(arr) == res
