'''
problem:
...
examples
input:
board = [
["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
output = true

assumptions, including constraints
    1. m,n can be really big
    2. word can start from anywhere
    3. don't go over something already used!

approaches: chiefly brute force and something better
    1. DFS at every node
        a. will need a visit data structure (can use matrix or set for this) for constraint 3
        b. at every node in traversal check that node-val == word[count]. end this traversal if it isn't
        note: let's set dfs up first
tradeoffs
...
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, col, curr):
            if curr == len(word):
                return True
            if (not(0 <= row < m and 0 <= col < n) or
                visit[row][col] or word[curr] != board[row][col]):
                return False
            res = False
            visit[row][col] = True
            for deltarow, deltacol in deltas:
                nextrow, nextcol = row + deltarow, col + deltacol
                res = res or dfs(nextrow, nextcol, curr + 1)
            visit[row][col] = False
            return res
                 
        deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]    
        m, n = len(board), len(board[0])
        visit = [[False for _ in range(n)] for _ in range(m)]
        res = False
        for row in range(m):
            for col in range(n):
                res = res or dfs(row, col, 0)
        return res