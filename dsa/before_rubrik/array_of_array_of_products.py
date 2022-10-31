from typing import List
def products_div(arr: List[int]) -> List[int]:
    prod = 1
    for x in arr:
        prod *= x
    res = [prod//x for x in arr]
    return res

'''
arr: [2, 3, 4, 5,]
l:   [2 23 234]
r:   [5 54 543]
res: [.-345, 2-45, 23-5, 234-.]

l = []
prod = 1
for i in range(len(arr)-1):
    prod *= arr[i]
    l.append(prod)
prod = 1
for i in range(len(arr)-1, 0, -1):
    prod *= arr[i]
    r.append(prod)
    
res = [1] * len(arr)
for i in range(len(arr) - 1):
    res[i] *= r[-i-1]
    res[i+1] = l[i]
return res
'''
def products(arr: List[int]) -> List[int]:
    l = []
    prod = 1
    for i in range(len(arr)-1):
        prod *= arr[i]
        l.append(prod)
    prod = 1
    r = []
    for i in range(len(arr)-1, 0, -1):
        prod *= arr[i]
        r.append(prod)
        
    res = [1] * len(arr)
    for i in range(len(arr) - 1):
        res[i] *= r[-i-1]
        res[i+1] = l[i]
    return res

arr = [2, 3, 4, 5,]
print(products(arr)) # [60, 40, 30, 24]
