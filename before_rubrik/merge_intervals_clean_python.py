'''    
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
-----
---
 ------
            --
                 -----
                 
result = [ ]
brute force is quadratic with intervals count

sorting
n lg n + n

intervals = copy(passed in intervals)
sort intervals
curridx = 0
while curridx != len(intervals) - 1 --------> use a foreach 
    if curr and curr + 1 intersect
        mark curr as deleted
        extend curr + 1 with curr
    curr = curr + 1
for all iintervals not deleted, add to result
S: O(n)
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def intersects(start1, end1, start2, end2):
            return min(end1, end2) - max(start1, start2) >= 0
        
        def union(start1, end1, start2, end2):
            return [min(start1, start2), max(end1, end2)]
            
        sortedintervals = sorted(intervals)
        for curridx in range(len(sortedintervals) - 1):
            if intersects(*sortedintervals[curridx], *sortedintervals[curridx + 1]):
                sortedintervals[curridx + 1] = union(*sortedintervals[curridx], *sortedintervals[curridx + 1])
                sortedintervals[curridx] = None
        return [interval for interval in sortedintervals if interval]
        
