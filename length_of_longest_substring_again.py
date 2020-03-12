class Solution:
    """
    10 mins to understand. at this point almost no code. \
    (pseudocode/notes is ok) should be written
    then hopefully if u got a good design; spend about 
    20-25 mins implementing a good solution.
    i mean don't try to finish in 2 mins. given who u are, that is just dumb!
    hitting the board with code or hammering the interviewer with 
    useless questions is a sure way to fail bcos: 
    - poor design (bad)
    - wrong design (worse)
    spend some time  with question/requirements. play around with it and have fun
    
    preserved
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        d=defaultdict(int)
        im,jm=0,-1
        i=0
        for j in range(len(s)):
            i=max(i,d[s[j]])
            if j-i > jm-im:
                im,jm=i,j
            d[s[j]]=j+1
        return jm-im+1
        
assert Solution().lengthOfLongestSubstring("abcabcbb")==3
assert Solution().lengthOfLongestSubstring("preserved")==4
assert Solution().lengthOfLongestSubstring("aaaaaa")==1
assert Solution().lengthOfLongestSubstring("abcdef")==6
assert Solution().lengthOfLongestSubstring("")==0

            