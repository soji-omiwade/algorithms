class Solution:
    def romanToInt(self, s: str) -> int:
        """
        35 - XXX V
        42 - XL II
        1764 - M D CC L X IV
        """
        res=0
        for i in range(len(s)-1,-1,-1):
            if s[i]=="M":
                res+=1000
            elif s[i]=="D":
                res+=500
            elif s[i]=="C":
                if res>=500:
                    res-=200
                res+=100
            elif s[i]=="L":
                res+=50
            elif s[i]=="X":
                if res>=50:
                    res-=20
                res+=10
            elif s[i]=="V":
                res+=5
            elif s[i]=="I":
                if res>=5: 
                    res-=2
                res+=1
        return res        
assert Solution().romanToInt("XXX V".replace(" ", "")) == 35
assert Solution().romanToInt("XL II".replace(" ", "")) == 42
assert Solution().romanToInt("M D CC L X IV".replace(" ", "")) == 1764
