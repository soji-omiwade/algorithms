class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #upper bound time: O(n)
        i = 0
        maxlen = 0
        have = set([])
        for j in range(len(s)):
            while s[j] in have:
                have -= {s[i]}
                i += 1
            have |= {s[j]}
            if j-i+1 > maxlen:
                maxlen = j-i+1
        return maxlen

sol = Solution()
s = "babad"; 
assert sol.lengthOfLongestSubstring(s) == 3
s = 'abracadabra'
assert sol.lengthOfLongestSubstring(s) == 4
s = ''
assert sol.lengthOfLongestSubstring(s) == 0
s = 'aaaaaaaaaa'
assert sol.lengthOfLongestSubstring(s) == 1
