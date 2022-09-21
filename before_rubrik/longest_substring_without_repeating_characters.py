'''
anxiety
impatience
distraction
'''
class Solution:
    def hold(self, s: str) -> int:
        #sadlamander
        if s == "":
            return 0
        i = ir = jr = 0
        bag = {}
        for j in range(len(s)):
            if s[j] in bag and bag[s[j]] >= i:
                i = bag[s[j]] + 1
            bag[s[j]] = j
            if j - i > jr - ir:
                ir, jr = i, j
        return jr - ir + 1
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sadlamander
        if s == "":
            return 0
        i = ir = jr = 0
        from collections import defaultdict
        bag = defaultdict(int)
        for j in range(len(s)):
            i = max(i, bag[s[j]])
            bag[s[j]] = j + 1
            if j - i > jr - ir:
                ir, jr = i, j
        return jr - ir + 1
        
assert Solution().lengthOfLongestSubstring("salamander") == 6
assert Solution().lengthOfLongestSubstring("sadlamander") == 6