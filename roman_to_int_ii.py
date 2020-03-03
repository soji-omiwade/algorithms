class Solution:
    def romanToInt(self, s: str) -> int:
        """
        35 - XXX V
        42 - XL II
        1764 - M D CC L X IV
        """
        res=0
        vxseen=lcseen=dmseen=False
        for i in range(len(s)-1,-1,-1):
            if s[i]=="M":
                res+=1000
                dmseen=True
            elif s[i]=="D":
                res+=500
                dmseen=True
            elif s[i]=="C":
                res+=100
                if dmseen:
                    res-=200
                lcseen=True
            elif s[i]=="L":
                res+=50
                lcseen=True
            elif s[i]=="X":
                res+=10
                if lcseen:
                    res-=20
                vxseen=True
            elif s[i]=="V":
                res+=5
                vxseen=True
            else:
                res+=1
                if vxseen:
                    res-=2
        return res        
assert Solution().romanToInt("XXX V".replace(" ", "")) == 35
assert Solution().romanToInt("XL II".replace(" ", "")) == 42
assert Solution().romanToInt("M D CC L X IV".replace(" ", "")) == 1764
