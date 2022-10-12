from typing import List
'''
array of array products
  - using pre and suffix arrays
  - one pass without pre and suffix arrays

[2, 7, 3, 4]
pre
1 1*2 2*7 2*7*3 2*7*3*4
suff
7*3*4*2 7*3*4 3*4 4*1 1
'''
def aa_prod_presuf(arr: List[int]) -> None:
    pre = [1] * (1 + len(arr)) #an extra element in front
    suff = [1] * (1 + len(arr)) #an extra element at back?
    for idx in range(1, len(pre)):
        pre[idx] = arr[idx - 1] * pre[idx - 1]
    for idx in range(len(suff) - 2, -1, -1):
        suff[idx] = arr[idx] * suff[idx + 1]
    for idx in range(len(arr)):
        arr[idx] = pre[idx] * suff[idx + 1]
    print(pre, suff)


def aa_prod_presuf_simple(arr: List[int]) -> None:
    assert(arr)
    pre = [arr[0]] * len(arr)
    suf = [arr[len(arr) - 1]] * len(arr)
    for idx in range(1, len(arr)):
        pre[idx] = pre[idx - 1] * arr[idx]
    for idx in range(len(arr) - 2, -1, -1):
        suf[idx] = arr[idx] * suf[idx + 1]
    for idx in range(1, len(arr) - 1):
        arr[idx] = pre[idx - 1] * suf[idx + 1]
    print(pre, suf)

#res = [12, 8, 24, 6]
arr = [2, 3, 1, 4]
print(arr)
aa_prod_presuf(arr)
print(arr)

arr = [2, 3, 1, 4]
aa_prod_presuf_simple(arr)
print(arr)

import sys
sys.exit()
#
#
#
#
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
