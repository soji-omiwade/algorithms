'''
time in:  11:52am
time out: 

"1", "2", ".", "1"
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            rowset = set([])
            for col, colval in enumerate(board[row]):
                if colval != "." and colval in rowset:
                    return False
                rowset.add(colval)
        for col in range(9):
            colset = set([])
            for row in range(9):
                rowval = board[row][col]
                if rowval != "." and rowval in colset:
                    return False
                colset.add(rowval)
        for rb in range(3):
            for cb in range(3):
                blockset = set([])
                for row in range(3):
                    for col in range(3):
                        val = board[rb*3 + row][cb*3 + col]
                        if val != "." and val in blockset:
                            return False
                        blockset.add(val)
        return True