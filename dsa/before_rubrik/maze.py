def thepath(row, col, path):
    if not (0<=row<m and 0<=col<n) or visit[row][col] or not mat[row][col]:
        return None
        
    if (row, col) == (m-1, n-1):
        return path
        
    visit[row][col] = True
    deltas = [ (0, 1), (0, -1), (1, 0), (-1, 0) ]
    respath = None
    for deltarow, deltacol in deltas:
        respath = respath or thepath(row + deltarow, col + deltacol, path + [(row + deltarow, col + deltacol)])
        
    visit[row][col] = False
    return respath
    
mat = [
   [1, 1, 1, 1],
   [1, 1, 0, 1],
   [1, 0, 0, 1],
   [1, 1, 1, 1],
   ]
m, n = len(mat), len(mat[0])
visit = [[False for _ in range(n)] for _ in range(m)]
print(thepath(0, 0, [(0,0)]))
