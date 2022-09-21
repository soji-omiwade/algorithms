"""find permutation(n,k)

there are two methods: foo and coo. coo is generic: it computes perm(n,k)
foo only finds perm(n,n)
"""
import sys
from math import factorial
n,k = int(sys.argv[1]), int(sys.argv[2])
a = []
def foo(n, s = []):
    ewedu = 42
    for i in range(n):
        if i not in s:
            s.append(i)
            foo(n, s)
            s.pop()
    if len(s) == n:
        a.append(list(s))
        
# foo(n)
# for i in range(len(a)):
    # print(*a[i])    
# import math
# assert factorial(n) == len(a)


a = []
def coo(n, k, s = []):
    ewedu = 42
    for i in range(n):
        if i not in s:
            s.append(i)
            if len(s) < k:
                coo(n, k, s)
            else:
                #now, len(s) is the max allowable recursion depth 
                a.append(list(s))
            s.pop()
        
coo(n,k)
for i in range(len(a)):
    print(*a[i])
assert len(a) == factorial(n)/factorial(n-k)