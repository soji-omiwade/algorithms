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
        def intersects(interv1, interv2):
            start1, end1 = interv1[0], interv1[1]
            start2, end2 = interv2[0], interv2[1]
            return min(end1, end2) - max(start1, start2) >= 0
        
        def union(interv1, interv2):
            start1, end1 = interv1[0], interv1[1]
            start2, end2 = interv2[0], interv2[1]
            return [min(start1, start2), max(end1, end2)]
            
        sortedintervals = sorted(intervals)
        for curridx in range(len(sortedintervals) - 1):
            if intersects(sortedintervals[curridx], sortedintervals[curridx + 1]):
                sortedintervals[curridx + 1] = union(sortedintervals[curridx], sortedintervals[curridx + 1])
                sortedintervals[curridx] = None
        return [interval for interval in sortedintervals if interval]
        
