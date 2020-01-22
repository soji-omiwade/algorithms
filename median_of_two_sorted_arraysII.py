from typing import List
from math import inf
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def median(a):
            n = len(a)
            return a[n//2] if n%2==1 else (a[n//2]+a[n//2-1])/2
        def merge(a,b):
            c = []
            i=j=k=0
            m,n = len(a),len(b)
            while k < m+n:
                ai = a[i] if i < m else inf
                bj = b[j] if j < n else inf
                if ai < bj:
                    c.append(ai)
                    i+=1
                else: 
                    c.append(bj)
                    j+=1
                k += 1
            return c
        c = merge(nums1,nums2)
        return median(c)

print(Solution().findMedianSortedArrays([1,2],[3,8,10,25,400]))