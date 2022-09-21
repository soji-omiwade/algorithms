def selection_sort(a):
    for i in range(len(a)-1): #at the start of iteration i, a[:i] is sorted
        min=a[i]
        for j in range(i+1,len(a)):
            if a[j] < min:
                min,a[j]=a[j],min
        a[i]=min
from random import shuffle
a=[i for i in range(100)]
shuffle(a)
assert a != [i for i in range(100)]
selection_sort(a)
assert a == [i for i in range(100)]
