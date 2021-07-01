def spiral_copy(inputMatrix):
  '''
  time: O(len(inputMatrix) * len(inputMatrix[0]))
  space: O(1) because no additional data structures
  '''
  top = left = 0
  bottom = len(inputMatrix) - 1
  right = len(inputMatrix[0]) - 1
  '''
  while true:
    if no more region:
      break
    go from left to right along top
    top += 1
    if no more region:
      break
    go from top to bottom along right
    right -= 1
    if no more region:
      break
    go from right to left along bottom
    bottom -= 1
    if no more region:
      break
    go from bottom to top along left
    left -= 1
  '''
  def invalid_region():
    return (bottom > top or right > left):
      
  res = []
  while True:
    if invalid_region(): break
    for i in range(left, right + 1):
      res.append(inputMatrix[top][i])
    top += 1
    if invalid_region(): break
    for i in range(top, bottom + 1):
      res.append(inputMatrix[i][right])
    right -= 1
    if invalid_region(): break
    for i in range(right, left - 1, -1):
      res.append(inputMatrix[bottom][i])
    bottom -= 1
    if invalid_region(): break
    for i in range(bottom, top - 1, -1):
      res.append(inputMatrix[i][left])
    left += 1
  return res