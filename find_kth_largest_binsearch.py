#relax
'''
constraint:
not k-th largest distinct

matrix = [
     [1,  5,  9]
    ,[2, 11, 13]
    ,[12, 13, 15]
]


2 4 8 8 8 14 16 18 20
k = 4 => result = 14
heap way:
put k in aheap
keep removing
'''
from typing import List
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        k -= 1
        n = len(matrix)
        div = k // n
        mod = k % n
        return matrix[div][mod]

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8      
print(Solution().kthSmallest(matrix, k)) #13