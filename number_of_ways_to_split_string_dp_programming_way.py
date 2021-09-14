class Solution:
    def numWays(self, s: str) -> int:
        # print(s)
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for lo in range(n):
            for hi in range(lo, n):
                dp[lo][hi] = (dp[lo][hi-1] if hi > lo else 0) + int(s[hi])
        
        count = 0
        for lo in range(1, n-1):
            for hi in range(lo + 1, n):
                count += dp[0][lo-1] == dp[lo][hi-1] == dp[hi][n-1]
        return int(count % (1e9 + 7))