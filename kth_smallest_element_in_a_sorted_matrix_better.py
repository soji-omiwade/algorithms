from pprint import pprint
from typing import List
from heapq import heapify, heappop, heappush
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        arr = [(lis[0], row, 0) for row, lis in enumerate(matrix)]
        pprint(arr)
        heapify(arr)
        for _ in range(k-1):
            _, row, col = heappop(arr)
            if col < n - 1:
                nextcolval, col = matrix[row][col + 1], col + 1
            else:
                nextcolval, col = float("inf"), 0
            heappush(arr, (nextcolval, row, col))
        return arr[0][0]

matrix = [
    [1,5,9]
    , [10,11,13]
    , [12, 14, 15]
]
print(Solution().kthSmallest(matrix, 8)) # 14

matrix = [
    [1,5,9]
    , [10,11,13]
    , [12, 14, 15]
]
print(Solution().kthSmallest(matrix, 7)) # 13