def spiral_copy(inputMatrix):
  def adjust_wall():
    # nonlocal wallleft, wallright, walltop, wallbottom
    d = direction[didx]
    if d == (0, 1): 
      nl.walltop += 1
    elif d == (1, 0):
      nl.wallright -= 1
    elif d == (0, -1):
      nl.wallbottom -= 1
    elif d == (-1, 0):
      nl.wallleft += 1
    else:
      raise Exception("impossible; direction doesnt exist")

  def within_walls():
    return (nl.wallleft <= col <= nl.wallright and
            nl.walltop <= row <= nl.wallbottom)
  class Nonlocal:
    pass
  nl = Nonlocal()
  nl.wallleft, nl.wallright = 0, len(inputMatrix[0]) - 1
  nl.walltop, nl.wallbottom = 0, len(inputMatrix) - 1
  direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
  didx = 0
  row = 0
  col = 0
  res = []
  for _ in range(len(inputMatrix[0]) * len(inputMatrix)):
      res.append(inputMatrix[row][col])
      row += direction[didx][0]
      col += direction[didx][1]
      if not within_walls():
        adjust_wall()
        row -= direction[didx][0]
        col -= direction[didx][1]
        didx = (didx + 1) % 4
        row += direction[didx][0]
        col += direction[didx][1]      
  return res    
 
inputMatrix  = [ [1,    2,   3,  4,    5],
                         [6,    7,   8,  9,   10],
                         [11,  12,  13,  14,  15],
                         [16,  17,  18,  19,  20] ]
print(spiral_copy(inputMatrix))