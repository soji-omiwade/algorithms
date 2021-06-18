'''
result = []
loop through all intervals interval with my newInterval
    if no overlap and we are passed newInterval
        break at idx
    if no overlap
        add interval
    else
        newInterval = union(newInterval, interval)
        
add newInterval

from idx to end
    add interval
    
t: O(n)
s: O(n)
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        iidx = 0
        for iidx, interval in enumerate(intervals):                                                     #1
            if min(interval[1], newInterval[1]) - max(interval[0], newInterval[0]) >= 0:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]          #1,5
            elif interval < newInterval:
                result.append(interval)
            else:
                break
        else:
            iidx += 1
        result.append(newInterval)
        for iidxp in range(iidx, len(intervals)):
            result.append(intervals[iidxp])
        return result
