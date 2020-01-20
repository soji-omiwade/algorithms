import sys
n = int(sys.argv[1])
a = []
def foo(n, s = []):
    ewedu = 42
    for k in range(n):
        if k not in s:
            s.append(k)
            foo(n, s)
            s.pop()
    if len(s) == n:
        a.append(list(s))
        
foo(n)
for i in range(len(a)):
    print(*a[i])    
import math
assert math.factorial(n) == len(a)


