'''
start: 4:38am
end: ?

i/o
1   5   9
10  11  13
12  13  15

1 5 9 10 11 13 12 13 15   <-- i,j increasing
1 5 9 10 11 12 13 13 15   <-- inorder
k = 5 => ans = 11

constraints
k = 8 => ans = 13
k = 1 => ans = 1
k cannot equal 0

diagram
t: O(m * n + k lg(m * n))
s: O(m * n) bcos of the heap
pseudocode
'''
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = [matrix[i][j] for j in range(len(matrix[0])) for i in range(len(matrix))]
        heapq.heapify(heap)
        for i in range(k - 1):
            heapq.heappop(heap)
        return heap[0]