class Solution:
    def intToRoman(self, num: int) -> str:
        """
        35 -> XXX V
        42 -> XL II
        1764 -> M D CC L X IV
        """
        letters="M CM D CD C XC L XL X IX V IV I".split()
        values=[ 1000,900,500,400,100,90,50,40,10,9,5,4,1 ]
        res=[]
        i=0
        while num>0:
            count = num // values[i]
            res.append(count*letters[i])
            num %= values[i]
            i+=1
        return "".join(res)
assert Solution().intToRoman(35) == "XXX V".replace(" ", "")
assert Solution().intToRoman(42) == "XL II".replace(" ", "")
assert Solution().intToRoman(1764) == "M D CC L X IV".replace(" ", "")
