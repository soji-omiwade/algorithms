def partition(a) -> int:
    i=-1
    for j in range(len(a)):
        if a[j] <= a[len(a)-1]:
            a[j], a[i+1] = a[i+1], a[j]
            i += 1
    return i
        
from random import shuffle, randrange
b=[i for i in range(100)]
x=randrange(100)
assert b[x] == x

shuffle(b)
k=partition(b)
assert b[k] == k
print(k)
print(b)

shuffle(b)
k=partition(b)
assert b[k] == k
print(k)
print(b)