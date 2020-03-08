def sort_sorted(a):
    i = -1
    for j in range(len(a)):
        if type(a[j]) is int:
            x = a[j]
            for k in range(j-1,i,-1):
                a[k+1] = a[k]
            a[i + 1] = x
            i += 1
    
a = [1, "cat", "dog", 3, "mouse", 4]
sort_sorted(a)
assert a == [1, 3, 4, "cat", "dog", "mouse"]

a = [1, 3, 4, "cat", "dog", "mouse"]
sort_sorted(a)
assert a == [1, 3, 4, "cat", "dog", "mouse"]

a = []
sort_sorted(a)
assert a == []

a = [str(x) for x in range(10)]
sort_sorted(a)
assert a == [str(x) for x in range(10)]

a = [x for x in range(10)]
sort_sorted(a)
assert a == [x for x in range(10)]
 
