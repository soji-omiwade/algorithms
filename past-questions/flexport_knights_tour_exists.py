"""
In chess, a knight moves in an L shape (1 square in any direction, then 2 squares in an orthogonal direction).

_ O _ O _
O _ _ _ O
_ _ X _ _
O _ _ _ O
_ O _ O _

Given W and H of the size of a chessboard, write a function that returns true if a knight placed at the top-left corner can be moved such that it touches every square exactly once.

1x1
X -> True

2x2
X0 -> False
00

2x3
X00 -> False
00_

00
00 -> False
00

X00 -> False
00_
000

3x4 ->

X___
____
____
____


X00
000
000
deltas = [
(1, 2), (-1, 2), 
(1, -2), (-1, -2), 
(2, 1), (-2, -1),
(-2, 1), (-2, -1)
]
goal = width * height
have = 0
visit = matrix[width, height] bool
return istour()

function istour(row=0, col=0)
    if row >= height or col >= width or visit[row][col]
        return False
        
    have += 1
    visit[row][col] = True
    if have == goal:
        return True  
    
    for delta in deltas
        if istour(row + delta[0], col + delta[1])
            return True
        
    have -= 1
    visit[row][col] = False
    return False
"""

def istour(width, height):
    def helper(row=0, col=0):
        nonlocal have
        if (not (0 <= row < height)
            or not (0 <= col < width)
            or visit[row][col]):
            return False
            
        have += 1
        path.append((row, col))
        visit[row][col] = True
        if have == goal:
            return True  
        
        for delta in deltas:
            if helper(row + delta[0], col + delta[1]):
                return True
            
        have -= 1
        path.pop()
        visit[row][col] = False
        return False

    deltas = [
    (1, 2), (-1, 2), 
    (1, -2), (-1, -2), 
    (2, 1), (-2, -1),
    (-2, 1), (-2, -1)
    ]
    path = []
    goal = width * height
    have = 0
    visit = [[False for col in range(width)] for row in range(height)]
    return path if helper() else None

for height in range(1, 5):
    for width in range(1, 5):
        if width <= height:
            print(width, height, istour(height, width))