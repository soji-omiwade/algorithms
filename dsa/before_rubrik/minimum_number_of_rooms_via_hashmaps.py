from collections import defaultdict
from typing import List

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, arr: List[int]):
        d = defaultdict(int)
        for start, end in arr:
            d[start] += 1
            d[end] -= 1
            
        ans = 0
        cnt = 0
        freqlookup = sorted(d.items())
        for inttime, intfreq in freqlookup:
            cnt += intfreq
            ans = max([ans, cnt])
        
        return ans

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

'''
freqlookup



freqlookup:
0: 1
5: 1
15: 1

30: -1
10: -1
20: -1

freqlookup: [ 0,1  5,1  10,-1  15,1  20,-1  30,-1]
cnt: 0 1 2 1 2 1 0
    
    

'''

a = [ [1, 18]   #------------------
    , [18,23]   #                  ----
    , [15,29]   #              ----------
    , [4, 15]   #    ----------
    , [2, 11]   # ----------
    , [5, 13]   #     -------
    ]
print(sol.solve(a)) # 4
