from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):                
                left=grid[i][j-1] if j>0 else "0"
                top=grid[i-1][j] if i>0 else "0"
                jp1_does_not_fall_over = j!=len(grid[0])-1 
                right=grid[i][j+1] if jp1_does_not_fall_over else "0"
                top_right=grid[i-1][j+1] if (jp1_does_not_fall_over and i !=0) else "0"
                if (grid[i][j]=="1" 
                    and left=="0" and top=="0"
                    and not (right=="1" and top_right=="1")):
                    count+=1
        return count