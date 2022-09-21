'''
X = T

. . . 
. . . 
. . . 

knight's tour 
'''
def tour(width: int, height: int, startrow: int=0, startcol: int=0) -> bool:
    def tour_helper(row, col, count):
        valid = 0 <= row < height and 0 <= col < width and not visit[row][col]
        if not valid:
            return False
        visit[row][col] = True
        # print(count)
        if count == width * height:
            return True
            
        is_tour = False
        for deltarow, deltacol in deltas:
            is_tour = is_tour or tour_helper(row + deltarow, col + deltacol, count + 1)
        visit[row][col] = False
        return is_tour
        
    deltas = [
        (1, 2), (1, -2),
        (-1, 2), (-1, -2),
        (2, 1), (2, -1),
        (-2, 1), (-2, -1)
    ]
    visit = [[False for col in range(width)] for row in range(height)]
    return tour_helper(startrow, startcol, 1)

for height in range(1, 5):
    for width in range(1, 5):
        if width <= height:
        # and (width, height) == (3, 4):
            print(width, height, tour(height, width))