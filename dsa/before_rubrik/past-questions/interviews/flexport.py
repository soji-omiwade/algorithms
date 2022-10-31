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

"""

def board(w, h):
    return [[False for _ in range(h)] for _ in range(w)]


deltas = [
    [1, 2], [1, -2],
    [-1, 2], [-1, -2],
    [2, 1], [2, -1],
    [-2, 1], [-2, -1]]

def go(a, w,h,x=0,y=0):
    print("w", w)
    print("h", h)
    print(a)
    if x<w and 0 <= x and 0 <= y and y<h:
        return False
    if a[x][y]: # from x,y
        return False
    a[x][y] = True
    
    all_true = True
    for i in range(w):
        for j in range(h):
            if not a[i][j]:
                all_true = False
    if all_true:
        return True
    
    for dx,dy in deltas:
        result = go(a,w,h,x+dx,y+dy)
        if result:
            return True

    a[x][y] = False
                
 
def foo(w,h):
    a = board(w,h)
    return go(a,w,h)

print(foo(2,3))
    