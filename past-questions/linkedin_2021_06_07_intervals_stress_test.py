from linkedin_2021_06_07_intervals import Intervals
from random import randrange
from pprint import pprint

'''
width = 5
count = 1000
for a count times
    start = rand between 0 and count - 1
    end = rand between start + 1 and count
'''
width = 5
count = 1000


intervals_types = (
    Intervals.init_as_bst(),
    Intervals.init_as_dll(),
    Intervals.init_as_list(),
    Intervals.init_as_set()
    )

import sys
if len(sys.argv) != 2:
    raise Exception(f"should be 2 args, not {len(sys.argv)}")
input_intervals = []
for _ in range(count):
    start = randrange(0, count - 2)
    end = randrange(start + 1, start + int(sys.argv[1]))
    input_intervals.append((start, end))
pprint(input_intervals)
prevres = None
for interval in intervals_types:
    for (start, end) in input_intervals:
        interval.addInterval(start, end)
        res = interval.getTotalCoveredLength()
        if prevres:
            assert prevres == res
