"""this version is made compatible to run in leetcode. 

it uses strings as the type of the sudoku elements and 
assumes there will always be one and only one solution 
per input
"""
n = 9
empty_cell_val = "."

def find_empty_cell(grid)->(int,int):
    """return a cell location that is still unassigned"""
    for i in range(n):
        for j in range(n):
            if grid[i][j] == empty_cell_val:
                return i,j
    return n,n

def is_safe(grid, row, col, val)->bool:
    """check whether it will be safe to assign val to specified location"""
    not_safe = in_row(grid, row, val) or in_col(grid, col, val) \
            or in_box(grid, row, col, val)
    return not not_safe
        
def in_row(grid, row, val):
    for c in range(n):
        if grid[row][c] == val:
            return True
    return False

def in_col(grid, col, val):
    for r in range(n):
        if grid[r][col] == val:
            return True
    return False
    
def in_box(grid, row, col, val):
    R, C = row//3, col//3
    for i in range(3):
        for j in range(3):
            if grid[3*R+i][3*C+j] == val:
                return True
    return False
       
def solve_sudoku(grid)->bool:
    r,c = find_empty_cell(grid)
    if (r,c) != (n,n):
        for val in range(ord("1"),1+ord(str(n))):
            chr_val = chr(val)
            if is_safe(grid, r, c, chr_val):
                grid[r][c] = chr_val
                if solve_sudoku(grid):
                    return True
                grid[r][c] = empty_cell_val
    else:
        return True
    #there is an empty cell, but I can't safely use it!
    return False        
    
def print_grid(grid):
    for i in range(n):
        print(*grid[i])

class Solution:

    #backtracking program to solve sudoku

    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        solve_sudoku(board)
        
if __name__ == "__main__":
    grid = \
        [[3, 0, 6, 5, 0, 8, 4, 0, 0], 
        [5, 2, 0, 0, 0, 0, 0, 0, 0], 
        [0, 8, 7, 0, 0, 0, 0, 3, 1], 
        [0, 0, 3, 0, 1, 0, 0, 8, 0], 
        [9, 0, 0, 8, 6, 3, 0, 0, 5], 
        [0, 5, 0, 0, 9, 0, 6, 0, 0], 
        [1, 3, 0, 0, 0, 0, 2, 5, 0], 
        [0, 0, 0, 0, 0, 0, 0, 7, 4], 
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

sudoku_solution = Solution()
print_grid(grid)
print()
sudoku_solution.solveSudoku(grid)
print_grid(grid)

