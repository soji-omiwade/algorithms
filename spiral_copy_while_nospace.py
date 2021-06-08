def spiral_copy(inputMatrix):
  def time_to_change_direction(row, col):
    return not (wall <= row + direction[didx][1] <= (m - 1) - wall and 
            wall <= col + direction[didx][0] <= (n - 1) - wall)
  
  def time_to_close_in_walls(row, col):
    return didx == 3 and col == wall and row == wall + 1
    
  m = len(inputMatrix)
  n = len(inputMatrix[0])
  res = []
  didx = row = col = wall = 0
  direction = ((1,0), (0, 1), (-1, 0), (0, -1))
  while len(res) < m * n:
    res.append(inputMatrix[row][col])
    if time_to_close_in_walls(row, col):
      wall += 1
    if time_to_change_direction(row, col):
      didx = (didx + 1) % 4
    row += direction[didx][1]
    col += direction[didx][0]
  return res

inputMatrix  = [ [1,    2,   3,  4,    5],
                         [6,    7,   8,  9,   10],
                         [11,  12,  13,  14,  15],
                         [16,  17,  18,  19,  20] ]

print(spiral_copy(inputMatrix))