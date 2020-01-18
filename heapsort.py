def left(i):
    return 2*i+1
    
def right(i):
    return 2*(i+1)
    
def extract_max(a, foo):
    mx = a[0]
    a[0] = a[foo]
    heapify(a, 0, foo)
    return mx
    
def heapify(a, i, n):
    l, r = left(i), right(i)
    largest = i
    if l < n and a[l] > a[largest]:
        largest = l
    if r < n and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, largest, n)

def build_max_heap(a):
    k = len(a)//2-1
    for i in range(k,-1,-1):
        heapify(a, i, n)
    
def heapsort(a):
    build_max_heap(a)
    count = len(a)
    while count:
        count -= 1
        a[count] = extract_max(a, count)
    return a
    
if __name__ == "__main__":
    import sys
    from random import choices
    n = int(sys.argv[1])
    a = choices(range(n),k=n)
    a_sorted = sorted(a)
    assert a_sorted != a 
    heapsort(a)
    assert a_sorted == a
    print(a)