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
        if p > r: 
            raise Exception('something went wrong:', p, r)
        q = (p + r)//2
        al = a[q-1] if q > 0 else -inf
        ar = a[q] if q < m else inf
        
        j = (m+n)//2 - q
        bl = b[j-1] if j > 0 else -inf
        br = b[j] if j < n else inf
        
        if max(al,bl) <= min(ar,br):
            if (m+n) % 2 == 0:
                return (max(al,bl)+min(ar, br))/2
            return min(ar, br)
        if ar < bl:
            return find_median(a, q+1, r, b)
        return find_median(a, p, q, b)
        
    if len(a) > len(b):
        a,b = b,a
    m,n = len(a),len(b)
    return find_median(a, 0, len(a), b)
        
if __name__ == "__main__":
    foo=[1,2,3,20,25]
    coo=[10,24,30,40,50]
    print(go(foo,coo))