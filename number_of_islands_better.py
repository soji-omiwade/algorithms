from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        m,n=len(grid),len(grid[0])
        def dfs(i,j):
            if (0<=i<m and 0<=j<n and grid[i][j] == "1"):
                grid[i][j]="#"
                dfs(i-1,j)
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i,j+1)
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count+=1
                dfs(i,j)
        return count



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
