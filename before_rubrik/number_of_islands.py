from typing import List
class Solution:

    class Node:
        def __init__(self):
            self.visited=False
            self.nbs=set([])
            
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def build_graph():
            g = []
            for i in range(m):
                g.append([])
                for j in range(n):
                    v=Solution.Node()
                    g[i].append(v)
                    if i-1>=0 and grid[i-1][j]==grid[i][j]:
                        g[i-1][j].nbs.add(v)
                        v.nbs.add(g[i-1][j])
                    if j-1>=0 and grid[i][j-1]==grid[i][j]:
                        g[i][j-1].nbs.add(v)
                        v.nbs.add(g[i][j-1])
            return g
            
        def dfs(v):
            if v.visited:
                return
            v.visited=True
            for w in v.nbs:
                dfs(w)
                
        m,n=len(grid),len(grid[0]) if len(grid)>0 else 0
        g=build_graph()
        island_count=0
        for i in range(m):
            for j in range(n):
                if not g[i][j].visited:
                    dfs(g[i][j])
                    if grid[i][j]=="1":
                        island_count+=1
        return island_count

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

print(Solution().numIslands(grid))
print(Solution().numIslands(gridII))
print(Solution().numIslands(gridIII))
