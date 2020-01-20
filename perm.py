import sys
n = int(sys.argv[1])
a = []
def foo(n, s):
    for k in range(n):
        if str(k) not in s:
            foo(n, s + str(k))
    if len(s) == n:
        a.append(s)
        
foo(n, "")
for i in range(len(a)):
    print(a[i])    
import math
assert math.factorial(n) == len(a)

