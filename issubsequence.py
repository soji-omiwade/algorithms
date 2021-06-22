'''
a c e
a b c d e

for ch in s
    keep going from last pos until find ch (or end of t)
if ch not at the end return false
else return true
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sidx = tidx = 0
        while sidx < len(s) and tidx < len(t):
            if s[sidx] == t[tidx]:
                tidx += 1
                sidx += 1
            else:
                tidx += 1
        return sidx == len(s)