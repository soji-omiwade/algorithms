class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        from math import sqrt
        lo = 0
        hi = int(sqrt(c)) + 1
        while lo <= hi:
            lo2 = lo**2
            hi2 = hi**2
            if lo2 + hi2 == c:
                return True
            if lo2 + hi2 < c:
                lo += 1
            else:
                hi -= 1
        return False
            
print(Solution().judgeSquareSum(2)) #False
print(Solution().judgeSquareSum(4)) #t
print(Solution().judgeSquareSum(3)) #f
print(Solution().judgeSquareSum(81920)) #t
print(Solution().judgeSquareSum(2**31-1)) #f