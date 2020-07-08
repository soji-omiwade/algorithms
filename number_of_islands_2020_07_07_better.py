from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandcount = 0
        def visitarea(r, c):
            if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c] == "1":
                grid[r][c] = "2"
                visitarea(r-1, c)
                visitarea(r+1, c)
                visitarea(r, c-1)
                visitarea(r, c+1)            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islandcount += 1
                    visitarea(i,j)
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
