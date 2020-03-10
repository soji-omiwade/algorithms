def quicksort(a,p,r,partition_type):
    def hoare_partition(a,p,r):
        x=a[p]
        i=p-1
        j=r+1
        while True:
            j-=1
            while a[j] > x:
                j-=1
            i+=1
            while a[i] < x:
                i+=1
            if i<j:
                a[i],a[j]=a[j],a[i]
            else:
                return j
    def simple_partition(a,p,r):
        x=a[r]
        i=p-1
        for j in range(p,r):
            if a[j]<=x:
                a[i+1],a[j]=a[j],a[i+1]
                i+=1
        a[i+1],a[r]=a[r],a[i+1]
        return i+1
    if (partition_type == "hoare" and p==r):
        return
    if (partition_type == "simple" and p>=r):
        return
    if partition_type == "hoare":    
        q=hoare_partition(a,p,r)
    else:
        q = simple_partition(a,p,r)
    if partition_type == "hoare":
        quicksort(a,p,q,partition_type)
    else:
        quicksort(a,p,q-1,partition_type)
    quicksort(a,q+1,r,partition_type)
    
    
    
from random import shuffle
count=100
a=[i for i in range(count)]
shuffle(a)
assert a != [i for i in range(count)]
quicksort(a,0,len(a)-1,"simple")
assert a == [i for i in range(count)]
