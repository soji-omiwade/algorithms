def mergesort(a,p,r):
    if p + 1 < r:
        q = (p+r)//2
        mergesort(a,p,q)
        mergesort(a,q,r)
        merge(a,p,r)
    
def merge(a,p,r,b = []):
    if b == []:
        b=[0 for _ in a]
    for i in range(p,r):
        b[i] = a[i]
    q = (p+r)//2
    lp, rp, count = p, q, 0
    while count < r-p:
        if rp == r or (lp < q and b[lp] < b[rp]):
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
    mergesort(a,0,n)
    assert sorted_a == a