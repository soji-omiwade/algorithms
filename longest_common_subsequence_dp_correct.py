class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1, text2 = "!" + text1, "!" + text2
        m, n = len(text1), len(text2)
        dp = [[0 for j in range(n)] for i in range(m)]
        for i, j in itertools.product(range(1, m), range(1, n)):
            if text1[i] == text2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]