'''
time: 10:59am
s = ! a b
t = ! a x x b 
s[:j] < t[:i] -->dp[j-1][i-1]
        equals s[:j-1] < t[:i-1] if s[j] == t[i] 
        equals s[:j] < t[:i-1]     if s[j] != t[i]
   
dp[i][j] == 0 for all i,j
s[:1] < t[:n] --> dp[0][i] = 1  for 0 <= i < n


1,1, 1,2 1,3, 1...m-1; 2,1 2,2 , ...

ij ... false
00 10 20 30 ...true
11: 00 01
12: 01 02
13: 02 03
21: 10 11
22: 11 12
23: 12 13

s[:j] < t[:i] == dp[j-1][i-1]
s[:1] < t[:1] == dp[0][0]

a        b
xxaxx    q 
a q c 
xxxaxxxb c  q     c

a b
xxxaxxb  c
for some j: 
s[:j+1]
control
s[:j+1] is sub of t[:i+1] <--> dp[i][j]


'''
from itertools import product
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s, t = "!" + s, "!" + t
        m, n = len(s), len(t)
        dp = [[True if j == 0 else False for j in range(m)] for i in range(n)]
        for (i, j) in product(range(1, n), range(1, m)):
            if t[i] == s[j]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j]
        return dp[-1][-1]