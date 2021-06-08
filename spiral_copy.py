def spiral_copy(input_matrix):
  COLMIN, ROWMIN = 0, 0
  COLMAX, ROWMAX = len(input_matrix[0]) - 1, len(input_matrix) - 1
  res = []
  row = col = 0
  n = len(input_matrix) * len(input_matrix[0])
  while len(res) < n:
    while col <= COLMAX:
      res.append(input_matrix[row][col])
      col += 1
    col -= 1
    ROWMIN += 1
    row += 1
    print(res, row, col)   
    while row <= ROWMAX:
      res.append(input_matrix[row][col])
      row += 1
    row -= 1
    COLMAX -= 1
    col -= 1
    print(res, row, col)
    while col >= COLMIN:
      res.append(input_matrix[row][col])
      col -= 1
    col += 1
    ROWMAX -= 1
    row -= 1
    print(res, row, col)
    while row >= ROWMIN:
      res.append(input_matrix[row][col])
      row -= 1
    row += 1
    COLMIN += 1
    col += 1
    print(res, row, col)
  return res

inputMatrix = [
  [1,    2,   3,  4,    5],
                         [6,    7,   8,  9,   10],
                         [11,  12,  13,  14,  15],
                         [16,  17,  18,  19,  20] ]
'''
[[1,2],[3,4]]
'''
print(spiral_copy(inputMatrix))