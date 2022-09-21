class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def max_pal(left: int, right: int):
            while left >=0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            left += 1
            right -= 1
            return left, right
        im, jm = 0, -1
        for i in range(n):
            lo, hi = max_pal(i, i)
            if hi - lo > jm - im:
                im, jm = lo, hi
            lo, hi = max_pal(i, i + 1)
            if hi - lo > jm - im:
                im, jm = lo, hi
        return s[im:jm+1]
assert Solution().longestPalindrome("noron") == "noron"
assert Solution().longestPalindrome("moqon") == "oqo"
assert Solution().longestPalindrome("moko") == "oko"
assert Solution().longestPalindrome("") == ""

assert Solution().longestPalindrome("noon") == "noon"
assert Solution().longestPalindrome("moon") == "oo"
assert Solution().longestPalindrome("moo") == "oo"

