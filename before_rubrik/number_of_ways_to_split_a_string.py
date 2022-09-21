class Solution:
    def numWays(self, s: str) -> int:
        n = len(s)
        res = 0
        onecount = [[1 if i==j and s[i] == "1" else 0 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                onecount[i][j] = onecount[i][j - 1] + int(s[j] == "1")
        
        for i in range(1, n - 1):
            for j in range(i+1, n):
                if onecount[0][i-1] == onecount[i][j-1] == onecount[j][n-1]:
                    res += 1
        return int(res % (1e9 + 7))