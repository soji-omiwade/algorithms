#backtracking program to solve sudoku

n = 9


    
def find_empty_cell(grid)->(int,int):
    """return a cell location that is still unassigned"""
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                return i,j
    return n,n

def is_valid_rc(grid, row, col)->bool:
    """check for validity of the grid with respect to row and col
    
    this means the row, column and box, corresponding to the parameters
    "row" and "col" do not violate sudoku rules.
    """
    is_valid = is_valid_row(grid, row) and is_valid_col(grid, col) \
            and is_valid_box(grid, row, col)
    return is_valid
        
def is_valid_row(grid, row):
    s = set([])
    zero_count = 0
    for c in range(n):
        if grid[row][c] == 0:
            zero_count += 1
        else:
            s.add(grid[row][c])
    if len(s) == n - zero_count:
        return True
    return False

def is_valid_col(grid, col):
    s = set([])
    zero_count = 0
    for r in range(n):
        if grid[r][col] == 0:
            zero_count += 1
        else:
            s.add(grid[r][col])
    if len(s) == n - zero_count:
        return True
    return False

def is_valid_box(grid, row, col):
    R, C = row//3, col//3
    zero_count = 0
    s = set([])
    for i in range(3):
        for j in range(3):
            if grid[3*R+i][3*C+j] == 0:
                zero_count += 1
            else:
                s.add(grid[3*R+i][3*C+j])
                
    if len(s) == n - zero_count:
        return True
    return False

def solve_sudoku(grid)->bool:
    r,c = find_empty_cell(grid)
    if (r,c) != (n,n):
        for val in range(1,1+n):
            grid[r][c] = val
            if is_valid_rc(grid, r, c) and solve_sudoku(grid):
                return True
            grid[r][c] = 0
    else:
        return True
    #there is an empty cell, but I can't safely use it!
    return False        
    
    
def print_grid(grid):
    for i in range(n):
        print(*grid[i])
        
if __name__ == "__main__":
    grid = \
        [[5, 0, 6, 5, 0, 8, 4, 0, 0], 
        [5, 2, 0, 0, 0, 0, 0, 0, 0], 
        [0, 8, 7, 0, 0, 0, 0, 3, 1], 
        [0, 0, 3, 0, 1, 0, 0, 8, 0], 
        [9, 0, 0, 8, 6, 3, 0, 0, 5], 
        [0, 5, 0, 0, 9, 0, 6, 0, 0], 
        [1, 3, 0, 0, 0, 0, 2, 5, 0], 
        [0, 0, 0, 0, 0, 0, 0, 7, 4], 
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    if solve_sudoku(grid):
        print_grid(grid)
