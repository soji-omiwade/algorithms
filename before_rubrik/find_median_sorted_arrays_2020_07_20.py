from typing import List
class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        m, n = len(a), len(b)
        if m > n:
            m, n = n, m
            a, b = b, a
        def binary_search_helper(p, r):
            i = (p+r)//2
            j = (m+n)//2 - i
            bjm1 = aim1 = float("-inf")
            ai = bj = float("inf")
            if j-1 >= 0:
                bjm1 = b[j-1]
            if i-1 >= 0:
                aim1 = a[i-1]
            if i < m:
                ai = a[i]
            if j < n:
                bj = b[j]
            if aim1 <= bj and bjm1 <= ai:
                if (m + n) % 2 == 1:
                    return min(ai, bj)
                return (max(aim1, bjm1) + min(ai, bj))/2
            if aim1 > bj: # => ai >= bjm1
                return binary_search_helper(p, i-1)
            #else, we have bjm1 > ai => bj >aim1
            return binary_search_helper(i+1, r)
        return binary_search_helper(0, m)

sol = Solution()
a = [1, 2, 3, 4]
b = [2, 3, 3, 8]
assert sol.findMedianSortedArrays(a, b) == 3
a = [1, 2, 4, 4]
b = [2, 3, 4, 8]
assert sol.findMedianSortedArrays(a, b) == 3.5
a = [1, 2, 3, 4]
b = [2, 4, 4, 8]
assert sol.findMedianSortedArrays(a, b) == 3.5
a = [1, 2, 4, 4]
b = [2, 3, 4]
assert sol.findMedianSortedArrays(a, b) == 3
a = [1, 2, 4, 40]
b = [20]
assert sol.findMedianSortedArrays(a, b) == 4