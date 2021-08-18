class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        def helper(row, column, depth) -> int:
            if not (depth <= k and 0 <= row < n and 0 <= column < n):
                return 0 

            if depth == k:
                return 1

            if mem[row][column][depth] != -1:
                # print('cache used at', row, column, depth, 'with value', mem[row][column][depth])
                return mem[row][column][depth]
            
            # print(' ' * 2 * depth, 'visit         ', row, column, staycount)
            staycount = 0
            for deltarow, deltacolumn in deltas:
                staycount += helper(row + deltarow, column + deltacolumn, depth + 1)
            mem[row][column][depth] = staycount
            # print(' ' * 2 * depth, 'backtrack from', row, column)
            return staycount
        
        mem = [[[-1 for depth in range(k+1)] for col in range(n)] for row in range(n)]
        # for row in range(n):
        #     for col in range(n):
        #         for depth in range(k + 1):
        #             mem[row][col][depth] = -1
                    
        deltas = [
            (1, 2), (-1, 2),
            (1, -2), (-1, -2),
            (2, 1), (2, -1),
            (-2, 1), (-2, -1)
        ]
        depth = 0
        space = 8 ** k
        staycount = 0
        for deltarow, deltacolumn in deltas:
            staycount += helper(row + deltarow, column + deltacolumn, depth + 1)
        return staycount / space if k != 0 else 1.0
    