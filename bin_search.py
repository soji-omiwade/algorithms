def go(a, p, r, key):
    global count
    count = 0
    return bin_search(a, p, r, key), count

def bin_search(a, p, r, key):
    global count
    count +=1
    if p == r: 
        return None
    q = (p+r)//2
    if a[q] == key: 
        return q
    if key < a[q]: 
        return bin_search(a, p, q, key)
    return bin_search(a, q+1, r, key)


