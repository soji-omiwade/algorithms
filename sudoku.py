def sudoku_solve(board):
  def isvalid_char(row, col, ch):
    for i in range(9):
      if board[row][i] != '.' and board[row][i] == ch: 
        return False
      if board[i][col] != '.' and board[i][col] == ch: 
        return False 
    row_blk = row // 3
    col_blk = col // 3
    for i in range(row_blk * 3, row_blk * 3 + 3):
      for j in range(col_blk * 3, col_blk * 3 + 3):
        if board[i][j] != '.' and board[i][j] == ch:
          return False
    return True
  
  def helper():
    for i in range(9):
      for j in range(9):
        if board[i][j] != '.':
          continue
        for k in range(1, 10):
          if isvalid_char(i, j, str(k)):
            board[i][j] = str(k)
            if helper():
              return True
            board[i][j] = '.'
        return False
    return True
    
  return helper()  

a = [[".",".",".","7",".",".","3",".","1"],["3",".",".","9",".",".",".",".","."],[".","4",".","3","1",".","2",".","."],[".","6",".","4",".",".","5",".","."],[".",".",".",".",".",".",".",".","."],[".",".","1",".",".","8",".","4","."],[".",".","6",".","2","1",".","5","."],[".",".",".",".",".","9",".",".","8"],["8",".","5",".",".","4",".",".","."]]          
print(sudoku_solve(a))