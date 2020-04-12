from number_of_islands_2020_06_04 import Solution
if __name__ == "__main__":
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
