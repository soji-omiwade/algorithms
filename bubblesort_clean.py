from random import shuffle
def bubblesort(a,k=1):
    for c in range(len(a)-1,-1,-1):
        for i in range(c):
            if a[i] > a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
        if k==c+1:
            return a[c]
            
a=["3", "1", "2", "dog", "mouse", "cat"]
bubblesort(a)
assert a == ["1", "2", "3", "cat", "dog", "mouse"]

a = ["1", "2", "3", "cat", "dog", "mouse"]
bubblesort(a)
assert a == ["1", "2", "3", "cat", "dog", "mouse"]

a = []
bubblesort(a)
assert a == []

a = [str(x) for x in range(10)]
shuffle(a)
bubblesort(a)
assert a == [str(x) for x in range(10)]

a = [x for x in range(10)]
shuffle(a)
bubblesort(a)
assert a == [x for x in range(10)]
 
