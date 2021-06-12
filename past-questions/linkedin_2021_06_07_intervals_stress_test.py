from linkedin_2021_06_07_intervals import Intervals
from random import randrange
from pprint import pprint
import timeit
import sys

'''
width = 5
count = 1000
for a count times
    start = rand between 0 and count - 1
    end = rand between start + 1 and count
'''
def test_compare_all_interval_types(intervals_types):
    prevres = None
    for interval in intervals_types:
        for (start, end) in input_intervals:
            interval.addInterval(start, end)
            res = interval.getTotalCoveredLength()
            if prevres:
                assert prevres == res

def time_compare_add_intervals(interval_type):
    res = []
    for (start, end) in input_intervals:
        interval_type.addInterval(start, end)

def time_compare_get_covered_length():
    interval_type.getTotalCoveredLength()

if len(sys.argv) != 2:
    raise Exception(f"should be 2 args, not {len(sys.argv)}")
count = 1000
input_intervals = []
for _ in range(count):
    start = randrange(0, count - 2)
    end = randrange(start + 1, start + int(sys.argv[1]))
    input_intervals.append((start, end))

intervals_types = (Intervals.init_as_bst(), Intervals.init_as_dll(),
                    Intervals.init_as_list(), Intervals.init_as_set())
reskeys = ["bst", "dll", "list", "set"]
res_vals = []
number = 100
for interval_type in intervals_types:
    addtime = timeit.timeit('time_compare_add_intervals(interval_type)',number=number, globals=globals())
    lentime = timeit.timeit('time_compare_add_intervals(interval_type)',number=number, globals=globals())
    res_vals.append((addtime, lentime))

pprint(dict(zip(reskeys, res_vals)))
# test_compare_all_interval_types()

