from collections import deque
def shortestCellPath(grid, sr, sc, tr, tc):
  width, height = len(grid), len(grid[0])
  arr1 = [(sr, sc)]
  arr2 = []
  count = 0
  while arr1:
    for loc in reversed(arr1): #doesn't matter whether it's reversed
      if loc == (tr, tc):
        return count
      locx, locy = loc[0], loc[1]
      left = locx - 1, locy
      right = locx + 1, locy
      top = locx, locy + 1
      bot = locx, locy - 1
      for nb in left, right, top, bot:
        if 0 <= nb[0] < width and 0 <= nb[1] < height and grid[nb[0]][nb[1]] == 1:
          arr2.append(nb)
          grid[nb[0]][nb[1]] = -1
    arr1, arr2 = arr2, []
    count += 1
  return -1  

grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
sr = 0
sc = 0
tr = 2
tc = 0
print(shortestCellPath(grid, sr, sc, tr, tc))


def shortestCellPath(grid, sr, sc, tr, tc):
  width, height = len(grid), len(grid[0])
  q = deque([(sr, sc)])
  count = 0
  while q:
    for _ in range(len(q)): #level
      loc = q.popleft()
      print("loc: ", loc)
      if loc == (tr, tc):
        return count
      locx, locy = loc[0], loc[1]
      left = locx - 1, locy
      right = locx + 1, locy
      top = locx, locy + 1
      bot = locx, locy - 1
      for nb in left, right, top, bot:
        if 0 <= nb[0] < width and 0 <= nb[1] < height and grid[nb[0]][nb[1]] == 1:
          q.append(nb)
          grid[nb[0]][nb[1]] = -1
    count += 1
  return -1  

grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
sr = 0
sc = 0
tr = 2
tc = 0
print(shortestCellPath(grid, sr, sc, tr, tc))
