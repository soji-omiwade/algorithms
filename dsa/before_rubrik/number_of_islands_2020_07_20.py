from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """time complexity: O(n^2)
        """
        count = 0
        def dfs_helper(r, c):
            if 0<=r<m and 0<=c<n and grid[r][c] == "1":
                grid[r][c] = "X"
                dfs_helper(r+1, c)
                dfs_helper(r-1, c)
                dfs_helper(r, c-1)
                dfs_helper(r, c+1)
                
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    dfs_helper(i, j)
        return count
sol = Solution()        
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
assert sol.numIslands(grid) == 1

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
assert sol.numIslands(grid) == 3