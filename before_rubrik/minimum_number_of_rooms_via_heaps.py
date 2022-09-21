from typing import List
from heapq import heappush, heappop

class Solution:
    def solve(self, arr: List[int]) -> int:
        arr = sorted(arr)
        harr = [arr[0][1]]
        for start, end in arr[1:]:
            print(harr)
            if start < harr[0]:
                pass
            else:
                heappop(harr)
            heappush(harr, end)
        return len(harr)
                
sol = Solution()
a = [ [0, 30]       #---------------------
    , [5, 10]       #   -----
    , [15,20] ]     #          ------
print(sol.solve(a)) # 2

a = [ [1, 18]   #------------------
    , [18,23]   #                  ----
    , [15,29]   #              ----------
    , [4, 15]   #    ----------
    , [2, 11]   # ----------
    , [5, 13]   #     -------
    ]
print(sol.solve(a)) # 4

'''
heap method:
1. sort input by start time
1b. add first interval, which makes it the smallest_end_time_interval
2. then for all other intervals
    if intersects(interval, smallest_end_time_interval)
        add a room 
    else
        discard the interval with smallest end time
    regardless: add interval
illustrating min-heap method:
at each iteration, new element added to heap
    ------------------1        1, 18 -- initialize heap; room added
     ----------2               2, 11 -- new end time interval = (2,11); room added
        ----------3            4, 15 -- room added
         -------4              5, 13 -- room added
                  ----------4  15,29 -- discard (2,11), making end time = (5,13); hence, no room added
                      ----4    18,23 -- discard (5,13), making end time = (4,15); hence, no room added
'''