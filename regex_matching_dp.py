'''
aab
a.b

aabab
aa

aa
aabab

aaaab
a*b

zero
aaaab
b

or more
aaab
a*b



0: b
1: ab
    

func ismatch(s, p)
    firstmatches = ...
    if p[1] == *
        if ismatch(s, p[2:])
            return True
        if ismatch(s[1:], p[0:])
    else
        return firstmatches and ismatch(s[1:], p[1:])
    
*-case (recursive)
    0 * case 
    try 1 -
no * case
'''
class Solution:
    def isMatch(self, string: str, pattern: str) -> bool:
        def helper(si, pi):
            if dp[si][pi] is not None:
                return dp[si][pi]
            if pi == n:
                return si == m

            firstmatches = si < m and pattern[pi] in (".", string[si])
            if pi + 1 < n and pattern[pi + 1] == "*":
                dp[si][pi + 2] = helper(si, pi + 2) # 
                if dp[si][pi + 2]:
                    return True
                if firstmatches:
                    dp[si + 1][pi] = helper(si + 1, pi)
                    if dp[si + 1][pi]:
                        return True
                return False
            else:
                if firstmatches:
                    dp[si + 1][pi + 1] = helper(si + 1, pi + 1) 
                    return dp[si + 1][pi + 1]
                return False
        m, n = len(string), len(pattern)
        dp = [[None for _ in range(1 + n)] for _ in range(1 + m)]
        return helper(0,0)
        
        
        