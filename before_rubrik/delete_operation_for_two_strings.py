'''
start: 10:12pm
end: 
i/o
 example:
 0 1 2 3
     t  
 ! s e a 
 ! e a t
 ans = 2.  
 
 
 derivation: 3 + 3 - 2 * lcss = 2. good  OR 4 + 4 - 2 * lcss = 2. good!
     b
 dp[0][bot] = 1
 dp[top][0] = 1
 dp[top][bot] = 
    if word1[top] == word2[bot] then 1 + dp[top - 1][bot - 1]
    else:                            max(dp[top - 1][bot], dp[top][bot - 1])
 len(word1) + len(word2) len(longest common sub)
  my example
  q e e a
  e e a t
  ans = 3
 constraints
diagram
. tabulate dp
. dp[top][bot] = 1 
pseudocode
    pad words with a '!'
    init dp to 1 when top or bot = 1; rest to 0
    after applying above alg. ans = 2 * word.lengths - (2 * dp[-1][-1])
test
! s
! a

1 1
1 0
    
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def lcss():
            for row in range(1, len(word2)):
                for col in range(1, len(word1)):
                    if word1[col] == word2[row]:
                        dp[row][col] = 1 + dp[row - 1][col - 1]
                    else:
                        dp[row][col] = max(dp[row][col - 1], dp[row - 1][col])
            return dp[-1][-1]
        
        word1 = '!' + word1
        word2 = '!' + word2
        dp = [[1 if 0 in (row, col) else 0 for col in range(len(word1))] for row in range(len(word2))]
        return len(word1) + len(word2) - 2 * lcss()
        