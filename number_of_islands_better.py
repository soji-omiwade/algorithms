from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        def remove_island(i,j):
            if (0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j] == "1"):
                grid[i][j]="#"
                remove_island(i-1,j)
                remove_island(i+1,j)
                remove_island(i,j-1)
                remove_island(i,j+1)
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count+=1
                remove_island(i,j)
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
