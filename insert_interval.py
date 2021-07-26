class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        3 pices
        first: all come before newInterval
        second: all overlap with newInterval
        third: do not overlap with newInterval
        '''
        def intersection(first, second):
            return min(second[1], first[1]) - max(second[0], first[0]) >= 0
        
        def union(first, second):
            return min(first[0], second[0]), max(first[1], second[1])
        
        result = []
        sidx = 0
        while sidx < len(intervals) and intervals[sidx][1] < newInterval[0]:
            result.append(intervals[sidx])
            sidx += 1
        
        while sidx < len(intervals) and intersection(newInterval, intervals[sidx]):
            newInterval = union(newInterval, intervals[sidx])
            sidx += 1            
        result.append(newInterval)        
        
        
        for i in range(sidx, len(intervals)):
            result.append(intervals[i])
            
        return result