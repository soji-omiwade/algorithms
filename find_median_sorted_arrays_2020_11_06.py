class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        def resfromvalidcut(aim1, bjm1, ai, bj):
            if (len(a) + len(b)) % 2 == 0
                return min(ai, bj)
            return (max(aim1, bjm1) + min(ai, bj)) / 2
            
        m, n = len(a), len(b)
        if m > n:
            a, b = b, a
            m, n = n, m
        for i in range(1, m):
            if a[i-1] <= b[j] and b[j-1] <= a[i]:
                return resfromvalidcut(a[i-1], b[j-1], a[i], b[j])
                
        #edge cases: i == 0 and i == m
        i = 0
        j = (m+n)//2
        if b[j-1] <= a[i]:
            bj = inf
            if n > m:
                bj = b[j]
            return resfromvalidcut(-inf, b[j-1], a[0], bj)
        i = m
        j = (m+n)//2 - i
        if a[m-1] <= b[j]:
            bjm1 = -inf
            if n > m:
                bjm1 = b[j-1]
            return resfromvalidcut(a[m-1], b[j-1], inf, b[j])
        raise Exception("median not found for some reason...")