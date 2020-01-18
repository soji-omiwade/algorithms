def mergesort(a,p,r):
    if p < r:
        q = (p+r)//2
        mergesort(a,p,q)
        mergesort(a,q+1,r)
        merge(a,p,r)
    
def merge(a,p,r,b = []):
    if b == []:
        b=[0 for _ in a]
    q = (p+r)//2
    for i in range(p,r+1):
        b[i] = a[i]
    lp, rp, count = p, q+1, 0
    while count < r-p+1:
        if rp > r or (lp <= q and b[lp] < b[rp]):
            a[count+p] = b[lp]
            lp += 1
        else:
            a[count+p] = b[rp]
            rp += 1
        count += 1
    
from random import randrange
from sys import argv
if __name__ == "__main__":
    n = int(argv[1])
    a = [randrange(n) for _ in range(n)]
    print(a)
    sorted_a = sorted(a)
    assert a != sorted_a
    mergesort(a,0,n-1)
    assert sorted_a == a