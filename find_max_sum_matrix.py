'''
Find the max-sum rectangle in a 2D matrix?
[1,   2,   -3],
[4,   -8,   -10],
[5,   6,    7],  


l r = l + r - 1 + cellval of right (from top to bot)


a[t][b][l][r] = a[t][b][l][r-1] + a[t][b][l][r]



dp[top, bot, left, right] = 
'''
from typing import List
def findsum_msr(matrix: List[List[int]]) -> int:       
    def findsum(top, bottom, left, right):
        if (top, bottom, left, right) in sumlookup:
            raise Exception("this would be weird")
            return sumlookup[top, bottom, left, right]
            
        res = 0
        for i in range(top, bottom + 1):
            for j in range(left, right + 1):
                res += matrix[i][j]
        sumlookup[top, bottom, left, right] = res
        return res
        
    maxsum = float("-inf")
    sumlookup = {}
    for rowtop in range(m):
        for rowbottom in range(rowtop, m):
            for colleft in range(n):
                for colright in range(colleft, n):
                    thesum = findsum(rowtop, rowbottom, colleft, colright)
                    print(thesum, rowtop, rowbottom, colleft, colright)
                    if thesum > maxsum:
                        maxsum, maxtop, maxbottom, maxleft, maxright = thesum, rowtop, rowbottom, colleft, colright
    return maxsum, maxtop, maxbottom, maxleft, maxright

matrix = [
[1,   2,   -3],
[4,   -8,   -10],
[5,   6,    7],   
]
m, n = len(matrix), len(matrix[0])
print(findsum_msr(matrix))