'''
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
        