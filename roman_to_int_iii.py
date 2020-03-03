class Solution:
    def romanToInt(self, s:str)->int:
        values=  [1, 4, 5, 9, 10,40,50,90,100,400,500,900,1000]
        symbols= "I IV V IX X XL L XC C CD D CM M".split(" ")
        res=0
        i=0
        while i<len(s):
            if s[i:i+2] in "IV IX XL XC CD CM".split(" "):
                res+= values[s[i:i+2]]
                i+=1
            else:
                res+=values[s[i]]
            i+=1
        return res
    
assert Solution().romanToInt("XXX V".replace(" ", "")) == 35
assert Solution().romanToInt("XL II".replace(" ", "")) == 42
assert Solution().romanToInt("M D CC L X IV".replace(" ", "")) == 1764
