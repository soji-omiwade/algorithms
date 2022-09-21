def spiral_copy(inputMatrix):
  m = len(inputMatrix)
  n = len(inputMatrix[0])
  res = []
  ccount = 0
  while ccount < (m + 1) // 2:
    for col in range(ccount, n - ccount):
      res.append(inputMatrix[ccount][col])
    for row in range(ccount + 1, m - ccount): #1, 1
      res.append(inputMatrix[row][n - 1 - ccount])
    if ccount < m // 2:
      for col in range(n - 1 - 1 - ccount, -1 + ccount, -1): #2, 0
        res.append(inputMatrix[m - 1 - ccount][col])
      for row in range(m - 1 - 1 - ccount, -1 + 1 + ccount, -1): # 1, 1
        res.append(inputMatrix[row][ccount])
    ccount += 1
  return res
  
inputMatrix  = [ [1,    2,   3,  4,    5],
                         [6,    7,   8,  9,   10],
                         [11,  12,  13,  14,  15],
                         [16,  17,  18,  19,  20] ]
res = [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]
print(spiral_copy(inputMatrix))
assert spiral_copy(inputMatrix) == res