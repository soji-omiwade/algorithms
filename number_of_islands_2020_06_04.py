from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        def visit_island(i, j):
            #if i and j valid and grid[i][j] is 1: then attempt to visit around
            if (0 <= i < len(grid) and 0 <= j < len(grid[0]) 
                    and grid[i][j] == "1"):
                grid[i][j] = "X"
                visit_island(i-1, j)
                visit_island(i+1, j)
                visit_island(i, j-1)
                visit_island(i, j+1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    island_count += 1
                    visit_island(i, j)
        return island_count
