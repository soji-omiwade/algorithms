class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def brute_force(s):
            n = len(s)
            mx = 0
            for i in range(n):
                for j in range(i+1,n):
                    sett = set([s[i]])
                    for k in range(i+1,j):
                        if s[k] in sett: 
                            break
                        sett.add(s[k])
                    lenn = len(sett)
                    if lenn > mx:
                        mx = lenn
                        im,jm = i,j
            return mx,im,jm
                   
        def sliding_window(s):
            i,j,mx,n=0,0,0,len(s)
            sett = set([])
            while i < n and j < n:
                if s[j] not in sett:
                    sett.add(s[j])
                    j+=1
                else:
                    while s[i] != s[j]:
                        sett.remove(s[i])
                        i += 1
                    sett.remove(s[i])
                    i+=1
                if j-i > mx:
                    mx,im,jm=j-i,i,j
            return mx,im,jm
        
        def sliding_window_with_dict(s):
            i,j,mx,n=0,0,0,len(s)
            from collections import defaultdict
            from math import inf
            d=defaultdict(lambda:-inf)
            while i < n and j < n:
                if d[s[j]] < i:
                    d[s[j]]=j
                    j+=1
                else:
                    i = d[s[j]]+1
                if j-i > mx:
                    mx,im,jm=j-i,i,j
            return mx,im,jm
        
        return sliding_window_with_dict(s)
            
for s in ("abcabcbb", "bbbbbbbb", "pwwkew"):
    print(s, Solution().lengthOfLongestSubstring(s), sep="-->")