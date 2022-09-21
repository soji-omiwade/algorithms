'''     
a = [1, 3, 3, 6, 6, 7, 9, ]
        . 
b = [2, 3, 5, 7]
     .
res = [1, 2, 5, 6, 6, 9]


a = [1, 2, 3, 3, 3, 6, 6, 7, 9, ]
                    . 
b = [2, 3, 3, 5, 7]
              .
        
res = [1, 5, 6, 6, 9]

1, 6, ...
2, ...
time: O(m + n)
space: O(m + n)

time: m lg n + n lg m
space: O(1)

time: O(m+n)
space: O(1)

corner case
    all the same
    two arrays are empty
'''
def remove_intersection(a, b):
    idxa = idxb = 0
    res = []
    while idxa < len(a) or idxb < len(b):
        aval = a[idxa] if idxa < len(a) else float("inf")
        bval = b[idxb] if idxb < len(b) else float("inf")
        if aval < bval:
            res.append(aval)
            idxa += 1
        elif aval > bval:
            res.append(bval)
            idxb += 1
        else:
            while idxa < len(a) and a[idxa] == aval:
                idxa += 1
            while idxb < len(b) and b[idxb] == bval:
                idxb += 1
    return res

a = [1, 3, 3, 6, 6, 7, 9, ]
b = [2, 3, 5, 7]
# res = [1, 2, 5, 6, 6, 9]
print(remove_intersection(a,b)) #

a = [5, 5, 5, 5, 5,]
b = [5,5,5,5,5,]
# res = []
print(remove_intersection(a,b))

a = []
b = []
# res = []
print(remove_intersection(a,b))

'''
good concurrency question
    set of producers ---------------- set of consumers.  ---->  i1  i2  

stock ticks
'''