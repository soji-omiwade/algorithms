a = []
n = int(input())
def foo(count, k, s):
    if count == 0:
        a.append(s)

    #starting from k, and incrementing, i can pick count times
    for _ in range(count):
        foo(count-1, (k+1)%n, s+str(k))
        k+=1
        
        
foo(n, 0, "")
import math
assert math.factorial(n) == len(a)
# for i in range(len(a)):
    # print(a[i])
