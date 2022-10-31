class Solution:
    def romanToInt(self, s: str) -> int:
        i=0
        res=0
        foo=cm,cd,xc,xl,ix,iv='cm','cd','xc','xl','ix','iv'
        coo=tuple("ivxlcdm")
        a = list(foo)+list(coo)
        b = [900,400,90,40,9,4,1,5,10,50,100,500,1000]
        d={}
        for rn,val in zip(a,b):
            d[rn]=val
        s=s.lower()
        while i < len(s):
            if s[i:2+i] in (cm,cd,xc,xl,ix,iv):
                res+=d[s[i:2+i]]
                i+=1
            else:
                res+=d[s[i]]
            i+=1
        return res