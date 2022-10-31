'''
a c e
a b c d e

look through t
pre process t with lookup for each char in s. ==> O(alphabet size + t.length)
for each schar, chidx in enumeration of s     ==> O(s.length * log t.length)
    get lookup for schar. (if it doesn't exist return false)
    curr = search (start=0, end = schar.lookup.length, curr) # return idx if found. otherwise, where you would place it 
    if curr is len(schar.lookup) return false
    curr += 1
return true
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #basic with a for
        sidx = 0
        for ch in t:
            if 0 <= sidx < len(s) and ch == s[sidx]:
                sidx += 1
        return sidx == len(s)