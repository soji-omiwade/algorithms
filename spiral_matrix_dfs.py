def spiral_matrix(inputMatrix):
    def legal_move():
        def move():
            nonlocal row, col
            row += direction[didx][1]
            col += direction[didx][0]
    
        nonlocal didx, row, col
        trow, tcol = row, col
        move()
        if not (0 <= row < m and 0 <= col < n and not visited[row][col]):
            didx = (didx + 1) % 4
            row, col = trow, tcol
            move()
            
    m = len(inputMatrix)
    n = len(inputMatrix[0])
    visited = [[False] * n for _ in range(m)]
    direction = ((1, 0), (0, 1), (-1, 0), (0, -1))
    didx = 0    
    res = []
    row = col = 0
    while len(res) < m * n:
        res.append(inputMatrix[row][col])
        visited[row][col] = True
        legal_move()
    return res
inputMatrix  = [         [1,    2,   3,  4,    5],
                         [6,    7,   8,  9,   10],
                         [11,  12,  13,  14,  15],
                         [16,  17,  18,  19,  20] ]

assert (spiral_matrix(inputMatrix) ==
[1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12])
assert spiral_matrix([[]]) == []
assert spiral_matrix([[1, 2],[4, 3]]) == [i for i in range(1, 5)]