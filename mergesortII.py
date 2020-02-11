"""i am repeating this as an exercise to properly setup a recursive base case"""
def mergesort(a):    
    def mergesort(a, p, r):
        nonlocal b
        if p == r:
            return

        mergesort(a,p,(p+r)//2)
        mergesort(a,(p+r)//2+1,r)
        merge(a,p,r,b)
    p,r = 0, len(a)-1
    b = [None for x in a]
    mergesort(a, p, r)
    return b

def merge(a, p, r, b):
    """merge (a, p, q) and (a, q+1, r)"""
    q = (p+r)//2
    
    i,j,count=p,q+1,p
    from math import inf
    while i<=q or j<=r:
        ai=aj=inf
        if i<=q:
            ai = a[i]
        if j<=r:
            aj = a[j]
            
        if ai < aj:
            b[count] = a[i]
            i+=1
        else:
            b[count] = a[j]
            j+=1
        count += 1
    for k in range(p,r+1):
        a[k] = b[k]
    
    
    
from random import shuffle
a = [i for i in range(10)]
b = list(a) 
shuffle(b)
print(b)
assert mergesort(b) == a