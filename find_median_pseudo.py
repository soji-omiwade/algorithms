'''
i/o
 representative example 
 constraints
talk...
pseudocode
(i + j) = (m + n) // 2
j = (m + n) // 2 - i

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

nums1 and nums2
[1|]
[3,4,5]
ans = 3

The overall run time complexity should be O(log (m+n)).


nums1
          ---90|400-
                i
nums2
-------------20|30-------
                j
check nums1[i] >= nums2[j - 1] and nums2[j] >= nums1[i - 1]. return either 
    min(nums1(i), nums2(j)) (if n + m is odd)
    average of max(nums1(i-1),nums2(j-1)) and min(nums1(i), nums2(j))
if nums1(i-1) > nums2(j) then i should move back!
otherwise i should move forward (which moves j back!)
 - m <= n ( to not miss any candidate while staying valid) i.e., i in [0, m]
    - so must treat case i == m special (can't array access there). if we binsearch, then we can check m first
    - moreover, i can make j in [0,n]. n happens (the one we care about) possibly when i = 0

while (i + j) # line 1

    j = ?


for i all elements in first array
    j = f(i)
    ...
    
nums1 and nums2
[1,2]
[3,4,5]
ans = 3

...
i/o
[1,3] [2,5]   <--- m and n
[1,2,3,5] = 2.5

[1,3], [2] = 2
constraints: n/a

diagram
O(n) time with O(n) add space 
[1,3] [2,5]
1) median is when half elements on left side. 
2a)  nums2[bot - 1] <= nums1[top]
2b)  nums1[top - 1] <= nums2[bot]

median = max(elment at top and bot - 1), and (min (top + 1, bot))
not needed: 2b)  nums1[top - 1] < botel 

     t
[1  3|]
    [|20  50]
    b 
top = 0, 
bot = 
[-- 2 3-- - ---]
------3 3------------------
n = m = 2
top = [0, m - 1]
bot   = (n + m) // 2 - top
median 
pseudocode

def get(arr, idx)
    if idx is negative
        return -inf
    if idx is len(arr)
        return inf
    return arr[idx]

O(n) time
for each element with idx top, find the bot as shown
    and check if that is your median wrt 3 conditions on 12 -- 14
    
O(log n)time
lo, hi = 0, len(nums1) <---ok due to line 33
while lo <= hi
    top = lo + (hi - lo) // 2
    bot = per line 29
    check per line 42
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def median_found():
            nums1top = inf
            if top != len(nums1):
                nums1top = nums1[top]
            nums1topm1 = -inf
            if top != 0:
                nums1topm1 = nums1[top - 1]
            nums2bot = inf
            if bot != len(nums2):
                nums2bot = nums2[bot]
            nums2botm1 = -inf
            if bot != 0:
                nums2botm1 = nums2[bot - 1]
            if nums1top >= nums2botm1 and nums2bot >= nums1topm1:
                return 0
            if nums1topm1 > nums2bot:
                return -1
            return 1       
                    
        def middle_element():
            nums1top = inf
            if top != len(nums1):
                nums1top = nums1[top]
            nums1topm1 = -inf
            if top != 0:
                nums1topm1 = nums1[top - 1]
            nums2bot = inf
            if bot != len(nums2):
                nums2bot = nums2[bot]
            nums2botm1 = -inf
            if bot != 0:
                nums2botm1 = nums2[bot - 1]
            if (n + m) % 2 == 1:
                return min(nums1top, nums2bot)
            return .5 * (max(nums1topm1, nums2botm1) + min(nums1top, nums2bot))

        from math import inf   
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
            
        for top in (0, m):
            bot = (m + n) // 2 - top
            if median_found() == 0:
                return middle_element()
            
        print("lets do it")
        lo, hi = 1, m - 1
        while lo <= hi:
            top = lo + (hi - lo) //2
            bot = (m + n) // 2 - top            
            found = median_found()
            if found == 0:
                return middle_element()
            if found == -1:
                hi = top - 1
            else:
                lo = top + 1
        raise Exception("Bug! Median should exist")