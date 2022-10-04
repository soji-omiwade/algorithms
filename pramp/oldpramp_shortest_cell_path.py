'''

[[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]

time: O(mn)
space: O(m+n) ...
'''
from collections import deque
def shortestCellPath(grid, sr, sc, tr, tc):
  nodes = deque([(sr, sc)])
  count = 0
  m, n = len(grid), len(grid[0])
  while nodes:
    for idx in range(len(nodes)):
      r, c = nodes.pop()
      grid[r][c] = 0
      if (r, c) == (tr, tc):
          return count
      
      deltas = [
        (1, 0), (-1, 0), (0, 1), (0, -1)
      ]
      for deltar, deltac in deltas:
        if 0 <= r+deltar < m  and 0 <= c+deltac < n and grid[r+deltar][c+deltac]:
          nodes.append((r+deltar, c+deltac))
    count += 1
  return -1


