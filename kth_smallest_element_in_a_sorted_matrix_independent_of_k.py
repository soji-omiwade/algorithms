from typing import List
'''
1 3 5
2 4 10
3 5 11
k = 5
1 2 3 3 *4* 5 5 10 11
mid = 6 => count = 7
predormid = 5 because largest number smaller than or equal to  mid = 4
succ = 10
count: number of elments smaller than or equal to mid 
count? 
    == k => then answer would be pre
    > k => mid too big => end = succ
    < k =>                start = pre
non-distinct: dont consider whether distinct

assume n x n matrix
heap: O(n + k lg n)

func bin-search
    start = mat[0][0]
    end = last elem
    while start <= end:
        mid = (start + end) // 2
        count, predormid, succ = countlessorequal(mid, predormid, succ)
        #count 3 elements less than mid
        if count == k:
            return predormid
        if count < k:
        

1 3 5
2 4 10
3 5 11
k = 5
1 2 3 3 *4* 5 5 10 11
mid = 6 => count = 7

'''

def kth_smallest(matrix: List[List[int]], k: int) -> int:
    def countlessorequal(mid):
        nonlocal predormid, succ
        count = 0
        row, col = n - 1, 0
        while row >= 0 and col < n:
            if matrix[row][col] <= mid:
                count += row + 1
                predormid = max(predormid, matrix[row][col])
                col += 1
            else:
                succ = min(succ, matrix[row][col])
                row -= 1
        return count
        
    n = len(matrix)
    if k > n * n or n == 0:
        raise ValueError
    if n == 1:
        return matrix[0][0]
    start = matrix[0][0]
    end = matrix[n-1][n-1]
    
    # import time
    while start < end: # not needed. we will find a k
        mid = (start + end) // 2
        predormid, succ = matrix[0][0], matrix[n-1][n-1]
        count = countlessorequal(mid)
        #count 3 elements less than mid
        # print(f"start = {start}, end = {end}, mid = {mid}, count = {count}", end='\t')
        # print(f"pre = {predormid}, succ = {succ}")
        if count == k:
            return predormid
        if count > k:
            end = predormid 
        else:
            start = succ 
        # time.sleep(.5)
    return start
     #1 2 5 7
        # p s
      # st    end
# m = 4
      
matrix = [            
    [1, 3, 5]
    , [2, 4, 10]
    , [3, 5, 11]
]
k = 5
print(kth_smallest(matrix, k))

'''
1 2 3 4 5
2 4 6 8 10
3 6 9 12 15
4 8
5 10
-> 1 2 2 3 3 4  4 4 5 5             6 6... 25
   st               start,p,m,end   s 
   
'''
from pprint import pprint
import sys
matrix = [[(i+1)*(j+1) for j in range(5)] for i in range(5)]
pprint(matrix)

k = 5
print(kth_smallest(matrix, k)) # 3

matrix = [[(i+1)*(j+1) for j in range(5)] for i in range(5)]
k = 9
print(kth_smallest(matrix, k)) # 5

