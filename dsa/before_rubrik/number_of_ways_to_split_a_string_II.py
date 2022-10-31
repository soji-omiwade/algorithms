'''
 0 0 0 0 
   1 2 3  
n-1 choose 2

n! / (n-r)! r! = 
'''
class Solution:
    def numWays(self, s: str) -> int:
        def zero(loc, count):
            need = 0   
            for i in range(loc, n):
                need += bool(int(s[i]))
                if need == count:
                    return i + 1
            raise Exception("zero: shouldnt be here")
        
        def one(loc):
            while s[loc] == '0':
                loc += 1
            return loc
        
        n = len(s)
        count = sum(int(ch) for ch in s)
        if count % 3 != 0:
            return 0
        if count == 0:
            return int(((n-1)*(n-2) // 2) % (1e9 + 7))
        divcount = count // 3
        '''
        01234567890123456789012345
        101010000110100001110
        a,b,c,d = 5,
        10101|0000|1101|0000|1110
              a    b    c    d
        '''
        a = zero(0, divcount)
        b = one(a)
        c = zero(b, divcount)
        d = one(c)
        return int((b-a+1) * (d-c+1) % (1e9 + 7))