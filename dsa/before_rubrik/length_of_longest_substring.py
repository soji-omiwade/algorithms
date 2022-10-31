class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j=0,0
        maxx = 0
        d = {}
        for j in range(len(s)):
            if s[j] in d:
                i = max(i,d[s[j]]+1)
            d[s[j]] = j
            old_max = maxx
            maxx = max(maxx,j-i+1)
            if maxx != old_max:
                im,jm = i,j
        return maxx,im,jm
        
print(Solution().lengthOfLongestSubstring("pwke4w3p"))