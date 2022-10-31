'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.
Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

    --
                        -----
                   ----
                                ----
        -----
new:        ---------
'''
def insert_interval(ints, newint):
    def intersection(start1, end1, start2, end2):
        # print(start1, end1, start2, end2)
        # print(min(end1, end2) - max(start1, start2))
        return min(end1, end2) - max(start1, start2) >= 0
        
    def merge(start1, end1, start2, end2):
        return min(start1, start2), max(end1, end2)
        
    newlist = []
    startnewint, _ = newint
    for idx, int in enumerate(ints):
        _, endint = int
        if endint < startnewint:
            newlist.append(int)
        else:
            nextstart = idx
            break
    else:
        nextstart = len(ints)
    print(newlist, end="\t")
    
    for idx in range(nextstart, len(ints)):
        int = ints[idx]
        if intersection(*newint, *int):
            # print('intersection', newint, int)
            newint = merge(*newint, *int)
        else:
            nextstart = idx
            break
    else:
        nextstart = len(ints)
    newlist.append(newint)       
    print(newlist, end="\t")
    
    for idx in range(nextstart, len(ints)):
        int = ints[idx]
        newlist.append(int)
    print(newlist)
    return newlist

intervals = [[1,3],[6,9]];
newInterval = [2,5]
print(insert_interval(intervals, newInterval))
# : [[1,5],[6,9]]

intervals = [[1,3],[6,9]];
newInterval = [22,25]
print(insert_interval(intervals, newInterval))
# : [[1,3],[6,9], [22,25]]

intervals = [[1,3],[6,9]];
newInterval = [0, 1]
print(insert_interval(intervals, newInterval))
# : [[0,3], [6,9]]
