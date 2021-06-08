def sort_k_messed_array(arr, k):
  rra = {arr[i]:i for i in range(k)}
  for i in range(len(arr) - 1):
    if i + k < len(arr):
        rra[arr[i+k]] = i + k
    mi = rra[min(rra)]
    arr[i], arr[mi] = arr[mi], arr[i]
    rra[arr[i]] = i
    rra[arr[mi]] = mi
    del rra[arr[i]]
  return arr

arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9, 0]
k = len(arr) - 1
print(sort_k_messed_array(arr, k))