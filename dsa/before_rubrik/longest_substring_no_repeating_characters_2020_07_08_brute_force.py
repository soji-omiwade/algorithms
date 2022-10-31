class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        for i in range(len(s)):
            for j in range(i+1, 1+len(s)):
                lschars = set([])
                for k in range(i, j):
                    old = len(lschars)
                    lschars.add(s[k])
                    if len(lschars) == old:
                        break
                    maxlen = max(len(lschars), maxlen)
        return maxlen

sol = Solution()
assert sol.lengthOfLongestSubstring("abracadabra") == 4
assert sol.lengthOfLongestSubstring("california") == 8
assert sol.lengthOfLongestSubstring("omiwade") == 7
assert sol.lengthOfLongestSubstring("") == 0
assert sol.lengthOfLongestSubstring("u") == 1