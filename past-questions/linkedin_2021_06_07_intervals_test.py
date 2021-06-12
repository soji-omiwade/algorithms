from linkedin_2021_06_07_intervals import Intervals

def test_iterate_bst():
    intervals_bst = Intervals.init_as_bst()
    input_ = ((8, 9), (1, 6), (4, 5), (1, 9), (0, 4), (20,40))
    for (from_, to) in input_:
        intervals_bst.addInterval(from_, to)
    for int_ in intervals_bst.ints:
        print(f"{int_}", end=", ")
    print()

def test(input_, res, intervals):
    for (from_, to), res in zip(input_, res):
        intervals.addInterval(from_, to)
        assert intervals.getTotalCoveredLength() == res
        
        
intervals_set = Intervals.init_as_set()
intervals_list = Intervals.init_as_list()
intervals_OrderedDLL = Intervals.init_as_OrderedDLL()
intervals_bst = Intervals.init_as_bst()

intervals_list.clear()
intervals_set.clear()
intervals_OrderedDLL.clear()
intervals_bst.clear()
input_ = ((8, 9), (1, 6), (4, 5), (1, 9), (0, 4))
res = (1, 6, 6, 8, 9)
test(input_, res, intervals_set)   
test(input_, res, intervals_list)   
test(input_, res, intervals_OrderedDLL)   
test(input_, res, intervals_bst)   

        
intervals_set = Intervals.init_as_set()
intervals_list = Intervals.init_as_list()
intervals_OrderedDLL = Intervals.init_as_OrderedDLL()
intervals_bst = Intervals.init_as_bst()

intervals_list.clear()
intervals_set.clear()
intervals_OrderedDLL.clear()
intervals_bst.clear()
input_ = ((8, 9), (1, 6), (4, 5), (1, 9))
res = (1, 6, 6, 8)
test(input_, res, intervals_set)   
test(input_, res, intervals_list)   
test(input_, res, intervals_OrderedDLL)   
test(input_, res, intervals_bst)   


intervals_list.clear()
intervals_set.clear()
intervals_OrderedDLL.clear()
intervals_bst.clear()
input_ = ((8, 9), (1, 6), (4, 5), (1, 9))
res = (1, 6, 6, 8)
test(input_, res, intervals_set)   
test(input_, res, intervals_list)   
test(input_, res, intervals_OrderedDLL)   
test(input_, res, intervals_bst)   


intervals_list.clear()
intervals_set.clear()
intervals_OrderedDLL.clear()
intervals_bst.clear()
input_ = ((1, 3), (9, 11), (2, 10))
res = (2, 4, 10)
test(input_, res, intervals_set)   
test(input_, res, intervals_list)   
test(input_, res, intervals_OrderedDLL)   
test(input_, res, intervals_bst)   

intervals_list.clear()
intervals_set.clear()
intervals_OrderedDLL.clear()
intervals_bst.clear()
input_ = ((1, 2), (50, 57), (10, 11), (1, 11))
res = (1, 8, 9, 17)
test(input_, res, intervals_set)   
test(input_, res, intervals_list) 
test(input_, res, intervals_OrderedDLL)   
test(input_, res, intervals_bst)   
