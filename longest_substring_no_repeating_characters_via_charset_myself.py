class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        pwkew
        """
        i=j=0
        im=jm=mx=0
        index = [0]*128
        for j in range(len(s)):
            i=max(i,index[ord(s[j])])
            index[ord(s[j])]=j+1
            val=j-i+1
            if val>mx:
                im,jm,mx=i,j,val
        return im,jm,mx
print(Solution().lengthOfLongestSubstring("pwkew"))