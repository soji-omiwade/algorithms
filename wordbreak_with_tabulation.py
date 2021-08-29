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
    tabulation
    table[i] = substring[i]
    abcde
    00 = t
    01 =  t/f
    02 = 01? and 2 = F
    03 = 02F
    0n
    
    f[0] = true
    for cvc = 1 .. n
        for k = 0 .. cvc
            f[cvc] = f[cvc] or ( s.substring(0, cvc) and f[k])
    return f[n]
    
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        f = [False] * (n + 1)
        words = set(wordDict)
        f[0] = True
        for cvc in range(1, n + 1): # 3 [_ _ _]
            for k in range(cvc+1): # 0 .. 3 --> 0, 1
                f[cvc] = f[cvc] or (s[k:cvc] in words and f[k])
        return f[n]
