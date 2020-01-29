def bin_search(a, x):
    def rbin_search(a, p, r, x)->bool:
        q = (p+r)//2
        if a[q] == x:
            return True
        if p == r-1:
            return False
        if x > a[q]:
            p = q + 1
        else:
            r = q - 1
        return rbin_search(a, p, r, x)
    return rbin_search(a, 0, len(a), x)
    
if __name__ == "__main__":
    foo=[1,2,3,20,25]
    coo=[10,24,30,40,50]
    foo.extend(coo)
    foo.sort()
    assert (True, False, False, True, True, True) == \
        (bin_search(foo,40), bin_search(foo,52), bin_search(foo,0), bin_search(foo,25), bin_search(foo,1), bin_search(foo,50))
        
        