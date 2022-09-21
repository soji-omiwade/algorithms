from typing import List
    
def spiral_matrix(inputMatrix: List[List[int]]):
    def next_():
        nonlocal row, col, didx, startrow, startcol, endrow, endcol
        didx %= 4
        if (didx == 0 and col == endcol):
            didx += 1
            startrow += 1
        elif (didx == 1 and row == endrow):
            didx += 1
            endcol -= 1
        elif didx == 2 and col == startcol:
            didx += 1
            endrow -= 1
        elif didx == 3 and row == startrow:
            didx += 1
            startcol += 1
        row += direction[didx % 4][1]
        col += direction[didx % 4][0]
        
    direction = ((1, 0), (0, 1), (-1, 0), (0, -1))
    didx = 0
    m, n = len(inputMatrix), len(inputMatrix[0])
    startrow = startcol = 0
    endrow, endcol = m - 1, n - 1
    res = []
    row = col = 0
    for count in range(m * n):
        res.append(inputMatrix[row][col])
        next_() #row, col out params
    return res
    
inputMatrix = [ 
[1, 2, 3], 
[4, 5, 6], 
[7, 8, 9]
]
inputMatrix = [[5 * i + j + 1 for j in range(5)] for i in range(4)]
from pprint import pprint
pprint(inputMatrix)
print(spiral_matrix(inputMatrix))