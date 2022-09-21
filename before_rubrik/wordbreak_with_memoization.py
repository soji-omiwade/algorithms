'''
2 ways:
1. consider all substrings, and use memoization to not reconsider substrings
leetcode
   ^
   
                              abcd
          a bcd                ab cd       abc d       abcd .
      /     |      \
   b cd   bc d    bcd .
   
n = s.length
helper(mid = 1)
function helper(mid)
    if mid == n:
        return True
    #s = orig-s[mid:]
    for idx in [mid ... n]
        if s.substring(0..idx) and helper(idx)
            return True
    return False

2. iteratively get the answer of whether s[i] can be segmented until i = n - 1
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def helper(lo):
            if lo == n:
                return True
            for mid in range(lo + 1, n + 1):
                if memo[mid] is None:
                    memo[mid] = helper(mid)
                if s[lo:mid] in words and memo[mid]:
                    return True
            return False
        
        n = len(s)
        memo = [None] * (n+1)
        words = set(wordDict)
        return helper(0)
        