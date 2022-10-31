from typing import List
from math import inf
class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        def median_helper(p, r):
            if p > r:
                return -1
            i = (p+r)//2
            j = (m+n)//2 - i
            if a[i-1] <= b[j] and b[j-1] <= a[i]:
                return i
            if a[i-1] > b[j]:
                return median_helper(p, i-1)
            return median_helper(i+1, r)
        m, n = len(a), len(b)
        if n < m:
            m, n = n, m
            a, b = b, a
        if len(a) != 0:
            i = median_helper(1, m-1)
            if i == -1:
                i = 0
                if b[(m+n)//2-1] > a[0]:
                    i = m
            aim1 = -inf if i == 0 else a[i-1]
            ai = inf if i == m else a[i]
        else:
            i = 0
            aim1 = -inf
            ai = inf
        j = (m+n)//2 - i
        bjm1 = -inf if j == 0 else b[j-1]
        bj = inf if j == n else b[j]
        if (n+m)%2 == 1:
            return min(ai, bj)
        return .5*(max(aim1,bjm1) + min(ai,bj))
    
median = Solution().findMedianSortedArrays
if __name__ == '__main__':
    a, b = [2,5], [1,10]
    assert median(a, b) == 3.5
    
    a, b = [2,5], [1]
    assert median(a, b) == 2
    
    a, b = [3,42], []
    assert median(a, b) == 22.5
    
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
    