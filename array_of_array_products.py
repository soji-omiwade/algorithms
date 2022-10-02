'''
arr = \

[2, 7, 3, 4]
 
 1 1 1 1
   2 2 2
 7   14 14
'''

def array_of_array_products(arr):
  if not arr or len(arr) == 1:
    return []
  output = []
  product = 1
  for idx in range(len(arr)):
    output.append(product) # [1*4*3*7  2*4*3  2*7*4  2*7*3] 
    product *= arr[idx]

  product = 1
  for idx in range(len(arr)-1, -1, -1):
    output[idx] *= product
    product *= arr[idx]

  return output

def quad__array_of_array_products(arr):
  if not arr or len(arr) == 1:
    return []
  output = [1] * len(arr)
  for primidx in range(len(arr)):
    for idx, idxelem in enumerate(arr):
      if idx != primidx:
        output[primidx] *= arr[idx]
  return output

arr = \
[2, 7, 3, 4]
print(array_of_array_products(arr))
