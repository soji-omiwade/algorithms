from typing import List
def median(a: List[int], b: List[int]) -> float:
    m, n = len(a), len(b)
    if n < m:
        m, n = n, m
        a, b = b, a
    for i in range(1, m):
        j = (m + n)//2 - i
        if a[i-1] <= b[j] and b[j-1] <= a[i]:
            break
    else:
        i = 0
        j = (m+n)//2
        if b[j-1] > a[0]:
            i = m
            j = (m+n)//2 - m
    from math import inf
    aim1 = -inf if i == 0 else a[i-1]
    ai = inf if i == m else a[i]
    bjm1 = -inf if j == 0 else b[j-1]
    bj = inf if j == n else b[j]
    if (n+m)%2 == 1:
        return min(ai, bj)
    return .5*(max(aim1,bjm1) + min(ai,bj))
    
if __name__ == '__main__':
    a, b = [2,5], [1,10]
    assert(median(a, b) == 3.5)
    
    a, b = [2,5], [1]
    assert(median(a, b) == 2)
    
    
    #random test
    import random
    random.seed(1)
    population = range(100)
    a = random.sample(population, 10)
    b = random.sample(population, 5)
    c = sorted(a + b)
    print(median(sorted(a), sorted(b)))
    print(c)
    assert c[7] == median(sorted(a), sorted(b))
    