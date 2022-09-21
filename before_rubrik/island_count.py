'''
Island Count
Given a 2D array binaryMatrix of 0s and 1s, implement a function getNumberOfIslands that returns the number of islands of 1s in binaryMatrix.

An island is defined as a group of adjacent values that are all 1s. A cell in binaryMatrix is considered adjacent to another cell if they are next to each either on the same row or column. Note that two values of 1 are not part of the same island if they’re sharing only a mutual “corner” (i.e. they are diagonally neighbors).

Explain and code the most efficient solution possible and analyze its time and space complexities.

Example:

input:  binaryMatrix = [ [0,    1,    0,    1,    0],
                         [0,    0,    1,    1,    1],
                         [1,    0,    0,    1,    0],
                         [0,    1,    1,    0,    0],
                         [1,    0,    1,    0,    1] ]

output: 6 # since this is the number of islands in binaryMatrix.
          # See all 6 islands color-coded below.
start: 10:09am
end: 


use graph
can we change the matrix?
create visited matrix
DFS
count = 0
function dfs(...)
    if not valid or visited ...or it is 0
        return
    visited[cell] = true
    dfs(cell left)
    dfs(cell to top, bottom, right)
    
for every cell in matrix
    if cell val == 1 ...and not visited!
        count ++
        dfs(cell)
return count
'''
def get_number_of_islands(binaryMatrix):
    def visit_island(row: int, col: int) -> None:
        if not (0 <= row < numrows and 0 <= col < numcols) or visited[row][col] or binaryMatrix[row][col] == 0:
            return
        visited[row][col] = True
        for drow, dcol in cells:
            visit_island(row + drow, col + dcol)

    cells = ((0, -1), (-1, 0), (0, 1), (1, 0))
    count = 0
    numrows, numcols = len(binaryMatrix), len(binaryMatrix[0])
    visited = [[False] * numcols for _ in range(numrows)]
    for row in range(numrows):
        for col in range(numcols):
            if not visited[row][col] and binaryMatrix[row][col] == 1:
                count += 1
                visit_island(row, col)
    return count
    
a = [[1,0],[1,0]]
a2 = [[1,0],[0,1]]
a6 = [ [0,    1,    0,    1,    0],
                         [0,    0,    1,    1,    1],
                         [1,    0,    0,    1,    0],
                         [0,    1,    1,    0,    0],
                         [1,    0,    1,    0,    1] ]
try:
    # x = get_number_of_islands(a)
    # assert x == 1
    x = get_number_of_islands(a2)
    assert x == 2
    # x = get_number_of_islands(a6)
    # assert x == 6
except:
    print(x)
    raise