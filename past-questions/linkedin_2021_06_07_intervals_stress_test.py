from linkedin_2021_06_07_intervals import Intervals
from random import randrange, shuffle
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
def functional_test():
    overlap = []
    prevres = None
    for interval in intervals_types:
        for (start, end) in input_intervals:
            interval.addInterval(start, end)
            interval.getTotalCoveredLength()
        res = interval.getTotalCoveredLength()
        overlap.append(interval.overlap_count)
        if prevres:
            assert prevres == res
        prevres = res
    pprint(dict(zip(reskeys, overlap)))
    
def time_compare_add_intervals(interval_type):
    res = []
    for (start, end) in input_intervals:
        interval_type.addInterval(start, end)

def time_compare_get_covered_length():
    interval_type.getTotalCoveredLength()

def rand_intervals():
    for _ in range(count):
        start = randrange(0, count - 2)
        end = randrange(start + 1, start + max_width)
        input_intervals.append((start, end))
    

def non_overlapping_intervals():
    '''
    start = 0
L1:    end = rand between start and max_width
    set start to end + 1
    go to L1 (unless count = 1000)
    '''
    start = 0
    for _ in range(1000):
        end = 1 + randrange(start, start + max_width)
        input_intervals.append((start, end))
        start = end
    shuffle(input_intervals)
    
intervals_types = (Intervals.init_as_bst(), Intervals.init_as_OrderedDLL(),
                    Intervals.init_as_list(), Intervals.init_as_set())
                    
def perf_test():
    res_vals = []
    number = 1
    for interval_type in intervals_types:
        addtime = timeit.timeit('time_compare_add_intervals(interval_type)',number=number, globals={**globals(), **locals()})
        lentime = timeit.timeit('time_compare_get_covered_length(interval_type)',number=number, globals={**globals(), **locals()})
        res_vals.append((addtime, lentime))
    pprint(dict(zip(reskeys, res_vals)))

if len(sys.argv) != 2:
    raise Exception(f"should be 2 args, not {len(sys.argv)}")
max_width = int(sys.argv[1])
count = 1000
input_intervals = []
reskeys = ["bst", "OrderedDLL", "list", "set"]
non_overlapping_intervals()
# rand_intervals()
# import sys
# print(sys.getrecursionlimit())
# sys.exit()
# sys.setrecursionlimit(1500)
functional_test()
# perf_test()

