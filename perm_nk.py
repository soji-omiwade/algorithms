def perm(s, k):
    def perm_helper(a, available, stamploc=0):
        if stamploc == k-1:
            for ch in available:
                a[-1] = ch
                res.append(''.join(a))
            return
        for ch in available:
            a[stamploc] = ch
            perm_helper(a, available - {ch}, stamploc + 1)
    if k == 0:
        return [None]
    res = []
    perm_helper([0 for _ in range(k)], set(s))
    return res
    
# print(sorted(perm("abc", 2)))
assert sorted(perm("abc", 2)) == [
'ab','ac', 'ba', 'bc', 'ca', 'cb'
]
# from pprint import pprint
# pprint([(i, val) for i,val in enumerate(perm('abcde',3))])

assert len(perm('ab', 1)) == 2
assert len(perm('abc', 2)) == 6
assert len(perm('abcd', 2)) == 12
assert len(perm('abcd', 4)) == 24
assert len(perm('abcde', 3)) == 60
def perm_len(n, k):
    from math import factorial
    return factorial(n)//factorial(n-k)
for i in range(6):
    print(f'6 perm {i}. expected:{perm_len(6,i)}. got {len(perm("abcdef", i))}')
    
