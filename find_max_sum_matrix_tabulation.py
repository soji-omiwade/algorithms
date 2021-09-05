'''
Find the max-sum rectangle in a 2D matrix?
[1,   2,   -3],
[4,   -8,   -10],
[5,   6,    7],  


l r = l + r - 1 + cellval of right (from top to bot)


a[t][b][l][r] = a[t][b][l][r-1] + a[t][b][r][r]
a[t][b][l][r] = t b l 

func foo(t b l r)
    if t b l r defines one cell (t == b and l == r) then return a[t b l r]
otherwise:
    t b l r = t b l (r-1)   +   t b r r
    t b l r = t (b-1) l r   +   b b l r

for t
    for b
        for l
            for r
                ...

dp[top, bot, left, right] = 
'''
from typing import List
def findsum_msr(matrix: List[List[int]]) -> int:       
    reason = "this is quite the same as memo except you take max for a given i, j as you go... nahh i dunno because it still uses memoization"
    reason += "i think the soln instead takes on the form res[row][col] = func(res[row-1][col], res[row][col-1], res[row-1][col-1])
    raise NotImplementedError(reason)
    
    maxsum = float("-inf")
    res = {}
    for top in range(m):
        for bot in range(top, m):
            for left in range(n):
                for right in range(left, n):
                    thesum = findsum(top, bot, left, right)
                    if thesum > maxsum:
                        maxsum, maxtop, maxbottom, maxleft, maxright = thesum, top, bot, left, right
    return res[m - 1, n - 1], maxtop, maxbottom, maxleft, maxright

matrix = [
[1,   2,   -3],
[4,   -8,   -10],
[5,   6,    7],   
]

m, n = len(matrix), len(matrix[0])
print(findsum_msr(matrix))