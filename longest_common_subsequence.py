'''
len(s) = m
len(t) = n
s[:], s[0:], s[1:m]
i --> s[i:] for 0 <= i < m
dp[i][j][k] --> s[:i+1][:j+1] < t[:k+1]   
0 <= j < len(substr(wrt i))
k 0 <= k < n 

ss < t  <--> dp[j][k]
if t[k] == ss[j] then dp[j][k] = dp[j-1][k-1]
else             then dp[j][k-1]
if dp[j][k]
    themax = max(themax, j + 1)

all subs start with None
dp[][0][k] = True
otherwise it's false

T: O(m^2 * n): mn + (m-1)n + (m-2)n + ... 1
S: O(mn)
constraints
s < t --> ease

'''
from pprint import pprint
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text2 = "!" + text2
        n = len(text2)
        themax = 0
        for i in range(len(text1)):
            sub = "!" + text1[i:]
            m = len(sub)
            dp = [[True if subidx == 0 else False for t2idx in range(n)] for subidx in range(m)]
            for (subidx, t2idx) in itertools.product(range(1,m), range(1,n)):
                if sub[subidx] == text2[t2idx]:
                    dp[subidx][t2idx] = dp[subidx - 1][t2idx - 1]
                else:
                    dp[subidx][t2idx] = dp[subidx][t2idx - 1]
                themax = max(themax, int(dp[subidx][t2idx]) * subidx)
            # print(themax)
            # pprint(dp)
        return themax