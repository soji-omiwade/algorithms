from typing import List
class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        if len(a) > len(b):
            a, b = b, a
        m, n = len(a), len(b)
        
        for i in range(m+1):
            j = (m+n)//2 - i
            aim1 = float("-inf") if i == 0 else a[i-1]
            bjm1 = float("-inf") if j ==0 else b[j-1]
            ai = float("inf") if i == m else a[i]
            bj = float("inf") if j == n else b[j]
            if (aim1 <= bj and bjm1 <= ai):
                if (m+n) % 2 ==1:
                    return min(ai, bj)
                return (max(aim1,bjm1) + min(ai,bj))/2

sol = Solution()
assert sol.findMedianSortedArrays([1,3], [2]) == 2
assert sol.findMedianSortedArrays([1,3,8,20], [2,5,10]) == 5
assert sol.findMedianSortedArrays([1,3], [2,4]) == 2.5
assert sol.findMedianSortedArrays([1,3,8,20], []) == 5.5
assert sol.findMedianSortedArrays([], [2,4,6,8,10]) == 6
