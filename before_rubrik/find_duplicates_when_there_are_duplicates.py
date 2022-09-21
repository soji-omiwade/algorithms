'''
time: 4:11pm -- 4:25pm = 14mins

assume dupplicates of any single element within any one given array, but not necessarily duplicated in other array

idx1 = idx2 = 0
while idx1 and idx2 are not past their resp. arrays
  get val1 and val2 (make it inf if one is at the end)
  if equal
    if not res
      res.append (val1)
    elif res[-1] != val1 #2nd cond to avoid duplicates in res!
      res.append(val1)
  elif val1 < val2
    idx1 ++
  else # both could be equal!
    idx2 ++ 
  3 3
  3 4
  
linear:
    time: O(m + n); space = O(1) + O(n) for res
binsearch:
    time: O(m lg n), where m <= n; space = same as above
'''

def find_duplicates_linear(arr1, arr2):
  idx1 = idx2 = 0
  res = []
  while idx1 < len(arr1) or idx2 < len(arr2):
    val1 = arr1[idx1] if idx1 < len(arr1) else float("inf") 
    val2 = arr2[idx2] if idx2 < len(arr2) else float("inf") 
    if val1 == val2:
      if not res or res[-1] != val1:
        res.append (val1)
      idx1 += 1
    elif val1 < val2:
      idx1 += 1
    else:
      idx2 += 1
  return res
    

def find_duplicates(arr1, arr2):
    def binsearch(key, lo, hi):
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if arr2[mid] == key:
                return True
            if arr2[mid] > key:
                hi = mid - 1
            else:
                lo = mid + 1
        return False
            
    res = []
    for key in arr1:
        if not res or res[-1] != key:
            if binsearch(key, 0, len(arr2)-1):
                res.append(key)
    return res
arr1 = [1, 1, 1, 2, 3, 5, 6, 6, 6, 7]
arr2 = [3, 6, 6, 6, 7, 8, 8, 8, 20]
print(find_duplicates(arr1, arr2)) # 3, 6, 7


