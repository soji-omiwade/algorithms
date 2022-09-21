class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        time: 6:25
        '''
        loc = {}
        lo = 0
        maxlen = 0
        for hi in range(len(s)):
            #make sure correct; lo: go one to the right of loc[hi]
            if s[hi] in loc and lo <= loc[s[hi]]:
                lo = loc[s[hi]] + 1
            #update location dict to include 
            loc[s[hi]] = hi
            # check if len is greater than maxlen
            if hi - lo + 1 >= maxlen:
                maxlen = hi - lo + 1
        return maxlen
        
go = Solution().lengthOfLongestSubstring
assert go("") == 0
assert go("abcabcbb") == 3
assert go("reserved") == 4
assert go("bbbbbb") == 1
