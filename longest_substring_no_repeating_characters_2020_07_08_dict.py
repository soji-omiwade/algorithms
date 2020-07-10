class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        locations = {}
        i = 0
        maxlen = 0
        for j in range(len(s)):
            if s[j] in locations:
                i = max(i, locations[s[j]] + 1)
            locations[s[j]] = j
            maxlen = max(maxlen, j-i+1)
        return maxlen
        
sol = Solution()
assert sol.lengthOfLongestSubstring("abracadabra") == 4
assert sol.lengthOfLongestSubstring("california") == 8
assert sol.lengthOfLongestSubstring("omiwade") == 7
assert sol.lengthOfLongestSubstring("") == 0
assert sol.lengthOfLongestSubstring("u") == 1