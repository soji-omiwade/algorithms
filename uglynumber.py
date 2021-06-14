class Solution:
    def isUgly(self, n: int) -> bool:
        '''
        if 1 then return True
        
        prime_factorize(n)
        if factorization contains anything other than 2,3 5 then we return false
                
        factorization(n)
        T:lg(n) + lg3(np) + lg5(npp) + ...
        '''
        if n <= 0:
            return False
        for prime in (2, 3, 5):
            while n % prime == 0:
                n //= prime
        res = False
        if n == 1:
            res = True
        return res
            