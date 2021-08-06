'''
space: O(lg k + kn) = O(kn)
time:  n * (1 * k + 2* k/2 + ... = n * (k lg k)
matrix size: 8n
                                     0,7->8n
             0,3->4n                                            4->4n
        0,1->2n      2,3->2n
      
    
contraints: 
    matrix could be empty or null

pseudocode:
    mergesort
func merge(arr1, arr2)
    always take the smaller of the two until both values are inf
    
func merge_arrays(matrix, lo, hi)
    if lo == hi: #len(maxtrix) is one
        return matrix[lo]
    if lo == hi - 1: #len(matrix) is two 
        return merge(matrix[lo], matrix[hi])
    #three or more:
    mid = lo + (hi - lo) // 2
    result = merge(merge_arrays(lo, mid), merge_arrays(mid+1, hi))
    return result
    
matrix = [
    [1,  5,  9],     _____________
    [0, 11, 11],                     ----------------------
        ...          _____________
    [4, 5, 19]      
]
result = [0,1,4,5,5,9,11,11,19]
'''

from typing import List, Optional
def merge_sorted_arrays(matrix: List[List[int]]) -> Optional[List[int]]:
    if not matrix:
        return None
    return _merge_sorted_arrays(matrix, 0, len(matrix) - 1)
    
def merge(arr1, arr2):
    #always take the smaller of the two until both values are inf
    '''
    i1
    1 2 5
    0 3 8
    i2
    '''
    from math import inf
    idx1 = idx2 = 0
    res = []
    len1, len2 = len(arr1), len(arr2)
    while idx1 < len1 or idx2 < len2:
        val1 = val2 = inf
        if idx1 < len1:
            val1 = arr1[idx1]
        if idx2 < len2:
            val2 = arr2[idx2]
        if val1 < val2:
            idx1 += 1
            val = val1
        else:
            idx2 += 1
            val = val2
        res.append(val)            
    print(arr1, arr2, res, end="assert check.....")
    assert len(res) == len(arr1) + len(arr2)
    print("done")
    return res
    
def _merge_sorted_arrays(matrix: List[List[int]], lo: int, hi: int) \
    -> List[int]:
    if lo == hi: #len(maxtrix) is one
        return matrix[lo]
    if lo == hi - 1: #len(matrix) is two 
        return merge(matrix[lo], matrix[hi])
    #three or more:
    mid = lo + (hi - lo) // 2
    result = merge(_merge_sorted_arrays(matrix, lo, mid), 
        _merge_sorted_arrays(matrix, mid+1, hi))
    return result
         
matrix = [
    [1,  5,  9], #    _____________
    [0, 11, 11],  #                   ----------------------
    #   ...           _____________
    [4, 5, 19]              
]
print(merge_sorted_arrays(matrix))
result = [0,1,4,5,5,9,11,11,19]
