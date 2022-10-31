class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.solve_sudoku(board)
        
    def isvalid(self, board, digit, row, column):
        for k in range(9):
            if digit in (board[row][k], board[k][column]):
                return False
        for r in range(3):
            r += (row // 3) * 3
            for c in range(3):
                c += (column // 3) * 3
                try:
                    if digit == board[r][c]:
                        return False
                except:
                    print(row, column, r, c)
                    raise
        return True
    
    def solve_sudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    continue
                for digit in range(1, 10):
                    digit = str(digit)
                    if self.isvalid(board, digit, row, col):
                        board[row][col] = digit
                        solved = self.solve_sudoku(board)
                        if solved:
                            return True
                board[row][col] = "."
                return False
        return True #no empty cell
        