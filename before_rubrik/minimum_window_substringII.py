from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        im,jm=0,len(s)
        d=defaultdict(int)
        abc_set=defaultdict(int)
        for ch in t:
            abc_set[ch]+=1
        i=0
        check=0
        for j in range(len(s)):
            if s[j] in abc_set:
                d[s[j]]+=1
                if d[s[j]] == abc_set[s[j]]:
                    check+=d[s[j]]
                    if check == len(t):
                        while True:
                            if s[i] not in abc_set:
                                i+=1
                            elif s[i] in abc_set and d[s[i]] > abc_set[s[i]]:
                                d[s[i]]-=1
                                i+=1
                            else:
                                break
                        if j-i<jm-im:
                            im,jm=i,j
                        check-=d[s[i]]
                        d[s[i]]-=1
                        i+=1
        if jm == len(s):
            return ""
        return s[im:jm+1]
