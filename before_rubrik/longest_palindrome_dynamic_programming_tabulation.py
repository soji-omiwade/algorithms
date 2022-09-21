class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        im, jm = 0, -1
        is_pal = [[False] * n for i in range(n)]
        for i in range(n):
            is_pal[i][i] = True
            im, jm = 0, 0
        for i in range(n-1):
            is_pal[i][i+1] = s[i] == s[i+1]
            if is_pal[i][i+1]:
                im, jm = i, i+1
        for i in range(2, n):
            for j in range(n-i):
                is_pal[j][i+j] = (s[j] == s[i+j]) and is_pal[j+1][i+j-1]
                if is_pal[j][i+j] and i > jm - im:
                    im, jm = j, i + j                    
        return s[im:jm + 1]
        
assert Solution().longestPalindrome("noron") == "noron"
assert Solution().longestPalindrome("moqon") == "oqo"
assert Solution().longestPalindrome("moko") == "oko"
assert Solution().longestPalindrome("") == ""

assert Solution().longestPalindrome("noon") == "noon"
assert Solution().longestPalindrome("moon") == "oo"
assert Solution().longestPalindrome("moo") == "oo"
        