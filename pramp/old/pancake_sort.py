def flip(arr, k): #k is the length of the subarray
  for i in range(k//2):
    arr[i], arr[k-i-1] = arr[k-i-1], arr[i]
    
def pancake_sort(arr):
  '''
  while array is unsorted
    largestidx = find idx largest  in unsorted array
    flip so that ends up in the first spot. 
    then flip unsorted subarray so that largest ends up at the end
  complexity: 
    O(n) for the while
    each flip in the while is O(n)
    hence complexity is O(n^2)
  '''
  def find_max_idx(arrlen):
    maxidx = 0
    maxval = arr[0]
    for i in range(arrlen):
      if arr[i] > maxval:
        maxidx, maxval = i, arr[i]
    return maxidx
  
  for i in range(len(arr)-1):
    maxidx = find_max_idx(len(arr) - i) #input is the length of the entire subarray
    flip(arr, maxidx + 1)
    flip(arr, len(arr) - i)
  return arr

res = [1,2,3]
a, b, c = res
print(a,b,c)
