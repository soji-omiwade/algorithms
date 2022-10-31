def perm(s, k):
    n = len(s)
    def perm_helper(a=None, stamploc=0, used=None):
        if a is None:
            a = [None] * k
        if used is None:
            used = [False] * n
        if stamploc == k-1:
            for i in range(n):
                if not used[i]:
                    a[stamploc] = s[i]
                    res.append(''.join(a))
            return
        for i in range(n):
            if not used[i]:
                a[stamploc] = s[i]
                used[i] = True
                perm_helper(a, stamploc+1, used)
                used[i] = False
    if k == 0:
        return [None]
    res = []
    perm_helper()
    return res
    
assert perm('abc', 1) == ['a', 'b', 'c']
assert perm('ab', 2) == ['ab', 'ba']
assert len(perm('abcdefg', 3)) == 210
assert perm('abc', 0) == [None]