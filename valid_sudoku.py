class Solution:
    def isValidSudoku(self, board) -> bool:
        
        for r in range(9):
            s = set([])
            for c in range(9):
                if board[r][c] != ".":
                    count = len(s)
                    s.add(board[r][c])
                    if count == len(s):
                        return False
                        
        for r in range(9):
            s = set([])
            for c in range(9):
                if board[c][r] != ".":
                    count = len(s)
                    s.add(board[c][r])
                    if count == len(s):
                        return False
                        
        for i in range(0,7,3):
            for j in range(0,7,3):
            # i = 3, j = 6
                s = set([])
                for ki in range(i, i+3):
                    for kj in range(j, j+3):
                        if board[ki][kj] != ".":
                            count = len(s)
                            s.add(board[ki][kj])
                            if count == len(s):
                                return False
        return True