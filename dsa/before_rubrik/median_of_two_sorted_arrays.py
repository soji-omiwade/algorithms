class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def merge(a,b):
            c = []
            i=j=0
            while i < len(a) or j < len(b):
                if i < len(a) and j < len(b):
                    if a[i] < b[j]:
                        c.append(a[i])
                        i+=1
                    else:
                        c.append(b[j])
                        j+=1
                elif i < len(a):
                    c.append(a[i])
                    i+=1
                else:
                    c.append(b[j])
                    j+=1
            return c
        a = merge(nums1,nums2)
        n = len(a)
        return a[n//2] if n%2==1 else (a[n//2]+a[n//2-1])/2