from typing import List
from itertools import chain

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if not matrix:
            return True
        m,n= len(matrix), len(matrix[0])
        idxs=chain(((i,0) for i in range(1,m)), ((0,j) for j in range(n)))
        for i,j in idxs:
            while 0<=k<m and 0<=j+1<n:
                if matrix[i+k][j+k] != matrix[i+1][j+1]:
                    return False
                i+=1; j+=1
        return True

assert Solution().isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]])
assert not Solution().isToeplitzMatrix([[1,2,4,4],[5,1,2,3],[9,5,1,2]])
assert not Solution().isToeplitzMatrix([[1,2],[2,2]])