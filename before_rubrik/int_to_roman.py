class Solution:
    def intToRoman(self, num: int) -> str:
       
       
        def foo(c,l,x,t):
            if t==0:
                res=""
            elif t<=3:
                res=t*x
            elif t<=5:
                res=(5-t)*x+l
            elif t<=8:
                res=l+(t-5)*x
            elif t==9:
                res=x+c
            return res
            
        m=num//1000
        h=(num%1000)//100
        t=(num%100)//10
        u=num%10
        
        res="m"*m
        #val and m,d,c; c,l,x; x,v,i
        res+=foo(*"mdc",h)
        res+=foo(*"clx",t)
        res+=foo(*"xvi",u)
            
        return res.upper()

import sys
print(Solution().intToRoman(int(sys.argv[1])))