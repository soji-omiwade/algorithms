"""
don't forget to check if the item foudn to be in the dict
is also in range [i, j)
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        mlen = min(len(s),1)
        d = {s[0]: 0} if len(s) > 0 else None
        for j in range(1,len(s)):
            if s[j] in d and d[s[j]] >= i: i = d[s[j]]+1
            d[s[j]] = j
            mlen = max(mlen,j-i+1)
        return mlen