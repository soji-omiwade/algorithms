class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        from math import log 
        if c == 0: 
            return True
        a = 0; b = 1
        
        logc = log(c)
        val = log (a*a + b*b)
        while val <= logc:
            print(a)
            while val <= logc:
                print('\t',a,b, val, logc)
                if abs(val - logc) < 1e-10:
                    return True
                b *= 2
                val = log (a*a + b*b)
            a += 1
            b = a
            val = log (a*a + b*b)
        return False
print(Solution().judgeSquareSum(81920))
print(Solution().judgeSquareSum(2**31-1))