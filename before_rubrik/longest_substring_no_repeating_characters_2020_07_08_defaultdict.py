from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        locations = defaultdict(int)
        i = 0
        maxlen = 0
        for j in range(len(s)):
            i = max(i, locations[s[j]])
            locations[s[j]] = j + 1
            maxlen = max(maxlen, j-i+1)
        return maxlen
        
sol = Solution()
assert sol.lengthOfLongestSubstring("abracadabra") == 4
assert sol.lengthOfLongestSubstring("california") == 8
assert sol.lengthOfLongestSubstring("omiwade") == 7
assert sol.lengthOfLongestSubstring("") == 0
assert sol.lengthOfLongestSubstring("u") == 1