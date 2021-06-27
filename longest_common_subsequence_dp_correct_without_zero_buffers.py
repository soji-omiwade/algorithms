'''
  a c e 
a 1 0 0 
b 0 0 0
c 0 0 0
d 0 0 0
e 0 0 0
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0 for j in range(n)] for i in range(m)]
        trigger = False
        for j in range(n): 
            if trigger or text1[0] == text2[j]:
                trigger = True
                dp[0][j] = 1
        trigger = False
        for i in range(m):
            if trigger or text1[i] == text2[0]:
                trigger = True
                dp[i][0] = 1            
        for i, j in itertools.product(range(1, m), range(1, n)):
            if text1[i] == text2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]