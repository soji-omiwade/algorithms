def sort_k_messed_array(arr, k):
  def minidx(arr, sidx):
    midx = sidx
    for i in range(sidx, min(sidx + k + 1, len(arr))):
      if arr[i] < arr[midx]:
        midx = i 
    return midx
    
  for i in range(len(arr)):
    mi = minidx(arr, i)
    arr[mi], arr[i] = arr[i], arr[mi]
  return arr
  
a = [1, 3, 0, 4, 2,]
k = 2
assert sort_k_messed_array(a, k) == [i for i in range(5)]