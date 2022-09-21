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
    def findsum(top, bot, left, right):
        global cachehit
        if (top, bot, left, right) in sumlookup:
            cachehit += 1
            print(cachehit)
            print(top, bot, left, right)
            return sumlookup[top, bot, left, right]
            
        res = 0
        if top == bot and left == right:
            res = matrix[top][left]
        elif top < bot:
            res = findsum(top, bot - 1, left, right) + findsum(bot, bot, left, right)
        elif left < right:
            res = findsum(top, bot, left, right - 1) + findsum(top, bot, right, right)
        else:
            raise Exception("bug: shouldnt be here")
        sumlookup[top, bot, left, right] = res
        return res
        
    maxsum = float("-inf")
    sumlookup = {}
    for top in range(m):
        for bot in range(top, m):
            for left in range(n):
                for right in range(left, n):
                    thesum = findsum(top, bot, left, right)
                    if thesum > maxsum:
                        maxsum, maxtop, maxbottom, maxleft, maxright = thesum, top, bot, left, right
    return maxsum, maxtop, maxbottom, maxleft, maxright

matrix = [
[1,   2,   -3],
[4,   -8,   -10],
[5,   6,    7],   
]
cachehit = 0
m, n = len(matrix), len(matrix[0])
print(findsum_msr(matrix), cachehit)