class Solution:
    def romanToInt(self, s: str) -> int:
        """
        35 - XXX V
        42 - XL II
        1764 - M D CC L X IV
        """
        res=0
        vseen=xseen=lseen=cseen=dseen=mseen=False
        for i in range(len(s)-1,-1,-1):
            if s[i]=="M":
                res+=1000
                mseen=True
            elif s[i]=="D":
                res+=500
                dseen=True
            elif s[i]=="C":
                res+=100
                cseen=True
                if dseen or mseen:
                    res-=200
            elif s[i]=="L":
                res+=50
                lseen=True
            elif s[i]=="X":
                res+=10
                xseen=True
                if lseen or cseen:
                    res-=20
            elif s[i]=="V":
                res+=5
                vseen=True
            else:
                res+=1
                if vseen or xseen:
                    res-=2
        return res        
assert Solution().romanToInt("XXX V".replace(" ", "")) == 35
assert Solution().romanToInt("XL II".replace(" ", "")) == 42
assert Solution().romanToInt("M D CC L X IV".replace(" ", "")) == 1764
