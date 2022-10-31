from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        class Node:
            def __init__(self):
                self.nbs = []
                self.visited = False
        g = {}
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    g[i,j] = Node()
                    if i-1 >= 0 and grid[i-1][j] == "1":
                        g[i-1,j].nbs += [g[i,j]]
                        g[i,j].nbs += [g[i-1,j]]
                    if j-1 >= 0 and grid[i][j-1] == "1":
                        g[i,j-1].nbs += [g[i,j]]
                        g[i,j].nbs += [g[i,j-1]]
                    
        islandcount = 0
        def dfs(v):
            "recursively visit nodes; v starts out unvisited"
            v.visited = True
            for w in v.nbs:
                if not w.visited:
                    dfs(w)
        for i,j in g:
            if not g[i,j].visited:
                islandcount += 1
                dfs(g[i,j])
        return islandcount

grid=[
["1","1","1","1","0"],
["1","1","0","1","0"],
["1","1","0","0","0"],
["0","0","0","0","0"]]
gridII=[
["1","1","0","0","0"],
["1","1","0","0","0"],
["0","0","1","0","0"],
["0","0","0","1","1"]]
gridIII=[
["1","1","1","1","1"],
["0","0","1","0","0"],
["1","1","1","1","1"]]

assert (Solution().numIslands(grid)) == 1
assert (Solution().numIslands(gridII)) == 3
assert (Solution().numIslands(gridIII)) == 1
