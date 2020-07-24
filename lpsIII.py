class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        lres, rres = 0, 0
        for m in (0, 1):
            for i in range(n):
                k = 0
                while (i-k >= 0 and i+k+m < n and s[i-k] == s[i+k+m]):
                    if 2*k+m > rres-lres:
                        lres, rres = i-k, i+k+m
                    k += 1
        return s[lres:rres+1]


assert Solution().longestPalindrome('a') == 'a'
assert Solution().longestPalindrome('bb') == 'bb'
assert Solution().longestPalindrome('car') == 'c'
assert Solution().longestPalindrome('cbbd') == 'bb'

assert Solution().longestPalindrome('bab') == 'bab'
assert Solution().longestPalindrome('qrbab') == 'bab'
assert Solution().longestPalindrome('qrbabst') == 'bab'

assert Solution().longestPalindrome('stqnoonr') == 'noon'