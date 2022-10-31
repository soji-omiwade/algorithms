'''

----
  -----
'''
from typing import Tuple

def union(from1, to1, from2, to2) -> Tuple[int, int]:
    return min(from1, from2), max(to1, to2)

'''
  ----
    ----
    
  ----
      ---
'''    
def intersection(from1, to1, from2, to2) -> bool:
    return max(from1, from2) - min(to1, to2) >= 0
    
'''
--
   -
           ---
               ---
                    ----
                          -----
      ----------
0) create a new array (need it to hold the resultant set)
1) find the idx where intersection first happens -> firstidx
    i.e., endi < fromint
2) from that idx go until you find the last intersecting lastidx
    i.e., starti > toint
    lastidx = that_idx 
3) capture the merged interval -> merged_interval
4) new array: intervals[0:firstidx] + [new element] + intervals[lastidx:]

'''
def add_interval(intervals, fromint, toint) -> None:

    for (idx, (_, toidx)) in enumerate(intervals):
        if toidx < fromint:
            firstidx = toidx
            break
    for idx in range(firstidx + 1, len(intervals)):
        idxfrom, end = intervals[idx]
        if toint < fromidx:
            lastidx = idx
            break
        else:
            fromint = min(fromint, idxfrom)
    return intervals[:firstidx] + new_interval + [lastidx:]
    