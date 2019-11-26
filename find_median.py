"""
find_median utilizes binary search. 
the difference here is we will always "find" the element, 
and so will converge without a check of p == r. 

note though that i did throw in an if just in case i got the logic wrong

if I find article for more details, i'll post it
"""
from math import inf
def go(a, b):
    def find_median(a, p, r, b):
        nonlocal m, n
        if p > r: 
            raise NameError('something went wrong:', p, r)
        q = (p + r)//2
        xL, xR = a[q-1] if q > 0 else -inf, a[q] if q < m else inf
        j = (m+n)//2 - q
        yL, yR = b[j-1] if j > 0 else -inf, b[j] if j < n else inf
        if max(xL,yL) <= min(xR,yR):
            if (m+n) % 2 == 0:
                return (max(xL,yL)+min(xR, yR))/2
            return min(xR, yR)
        if xR < yL: #if so, then we should go right
            return find_median(a, q+1, r, b)
        return find_median(a, p, q, b)
        
    if len(a) > len(b):
        a,b = b,a
    m,n = len(a),len(b)
    return find_median(a, 0, len(a), b)
        