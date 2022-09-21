def sudoku_solve(board):
    '''
    go through every time (left to right, top to bottom), iteratively 
    adding *valid* items.  that is:
    for the next available board item
        for each valid number
            add a valid number
            ok = recursively go to the next item
            if ok
                return True
        return False
    return True
    '''
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                for k in range(1, 10):
                    ch = str(k)
                    if isvalid(board, ch, i, j):
                        board[i][j] = ch
                        if sudoku_solve(board):
                            return True
                        board[i][j] = '.'
                return False
    return True
    
def isvalid(board, ch, row, col):
    srow = row // 3 * 3
    scol = col //3 * 3
    for i in range(9):
        if ch in (
            board[srow + i // 3][scol + i % 3],
            board[row][i],
            board[i][col]):
            return False
    return True

a = [[".",".",".","7",".",".","3",".","1"],["3",".",".","9",".",".",".",".","."],[".","4",".","3","1",".","2",".","."],[".","6",".","4",".",".","5",".","."],[".",".",".",".",".",".",".",".","."],[".",".","1",".",".","8",".","4","."],[".",".","6",".","2","1",".","5","."],[".",".",".",".",".","9",".",".","8"],["8",".","5",".",".","4",".",".","."]]          
print(sudoku_solve(a))