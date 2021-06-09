'''
Question : 1
    
    
public interface Intervals {
 
    /**
     * Adds an interval [from, to) into an internal structure.
     */
    void addInterval(int from, int to);
 
    /**
     * Returns a total length covered by the added intervals.
     * If several intervals intersect, the intersection should be counted only once.
     * Example:
     *
     * addInterval(3, 6)
     * addInterval(8, 9)
     * addInterval(1, 5)
     
        addInterval(4, 5)
     *
     * getTotalCoveredLength() -> 6
     *
     * i.e. [1,5) and [3,6) intersect and give a total covered interval [1,6) with a length of 5.
     *      [1,6) and [8,9) don't intersect, so the total covered length is a sum of both intervals, that is 5+1=6.
     *          *f     *t       
     *          |__|__|__|                  
     *                         |__|         (8,9) 
     *    |__|__|__|__|                     (1,6) 
                                            (4,5)
     *
     * 0  1  2  3  4  5  6  7  8  9  10
     *
     */ 
    int getTotalCoveredLength();
 
}
'''
from typing import Tuple, Set
class Intervals:
    def __init__(self):
         self.ints = None

    @classmethod
    def init_as_set(cls):
        intervals = cls()
        intervals.ints = set([])
        return intervals
        
    @classmethod
    def init_as_list(cls):
        intervals = cls()
        intervals.ints = []
        return intervals
        
    @staticmethod
    def _intersects(top, bot):
        return min(top[1], bot[1]) > max(top[0], bot[0])
        
    def clear(self):
        self.ints.clear()
        
    def addInterval(self, *args):
        if type(self.ints) is list:
            self.addInterval_list(*args)
        elif type(self.ints) is set:
            self.addInterval_set(*args)
        else:
            raise NotImplementedError()
        
    def addInterval_list(self, from_, to):
        '''
        what is going on?! now realizing this won't work if there's stuff in
        between that is not part of i. in which case the ff problems arise:
        - u dont get to nullify the correct location
        - u nullified a location you shouldn't 
        code breaking example:
        (1, 2), (50, 67), (10, 11), (1, 11)
        
        [(1,11), (50,67), (10, 11), (1,11)]
        expected: 10 + 7 = 17
        would get: ... just fixed the code, and now it's much simpler
        '''
        for i, (from_curr, to_curr) in enumerate(self.ints): #O(n)
            if self._intersects((from_, to), (from_curr, to_curr)):
                from_, to = min(from_, from_curr), max(to, to_curr)
                self.ints[i] = None
        self.ints.append((from_, to))
        self.ints = [int_ for int_ in self.ints if int_]           

    def addInterval_set(self, from_, to):
        '''
        this is wrong: the code above shows how to do it right.
        failing case.
        order of incoming intervals: (1, 3), (9, 11), (2, 10)
        expected: 11
        (1, 3)
        (9, 11) 
        (2, 10)--> 
                --> from_,to is now (1, 10) after iterating on (1,3)
                --> now iterate on (9, 11). at ln 86, f, t =  join (1, 10)  and (9, 11) --> (1, 11). But already we added  (1, 10) to the set!
                --> so like above, from_, to, should not forget the last item that was added and check that it isn't a subset of it. 
                --> suffices to check intersect. but what we really need to do here (and in addInterval_list) is check subset!
        code below will have (1, 11) and (2
        '''
        for from_curr, to_curr in self.ints.copy(): #O(n)
            if self._intersects((from_, to), (from_curr, to_curr)):
                from_, to = min(from_, from_curr), max(to, to_curr)
                self.ints.remove((from_curr, to_curr))
        self.ints.add((from_, to))

    def addInterval_set_lite(self, from_, to):
        '''
        ---
              ----
                           ---
           ---------
        type of ints as set
        to_remove as set
        for each int_ in ints:
            if from_, to intersect with int_
                to_remove.add(int_)
                from_, to = union_of(int_, from_, to)
        remove all items in to_remove from ints
        add from_, to to ints
        input_ = ((8, 9), (1, 6), (4, 5), (1, 9))
        res = (1, 6, 6, 8)
        '''
        ints_to_remove = set()
        for int_ in self.ints:
            if self._intersects((from_, to), int_):
                ints_to_remove.add(int_)
                from_, to = min(from_, int_[0]), max(to, int_[1])
        self.ints = self.ints.difference(ints_to_remove)
        self.ints.add((from_, to))
        
    def addInterval_heap(self, new_from, new_to):
        raise NotImplementedError
        
    def getTotalCoveredLength(self) -> int:
        reslen = 0
        for (from_, to) in self.ints:
            reslen += to - from_
        return reslen    

def test(input_, res, intervals):
    for (from_, to), res in zip(input_, res):
        intervals.addInterval(from_, to)
        assert intervals.getTotalCoveredLength() == res

intervals_set = Intervals.init_as_set()
intervals_list = Intervals.init_as_list()

input_ = ((8, 9), (1, 6), (4, 5), (1, 9))
res = (1, 6, 6, 8)
import timeit
print(min(timeit.repeat('intervals_set.clear()\ntest(input_, res, intervals_set)', 'from __main__ import test, input_, res, intervals_set')))
print(min(timeit.repeat('intervals_list.clear()\ntest(input_, res, intervals_list)', 'from __main__ import test, input_, res, intervals_list')))
# test(input_, res, intervals_set)   
# test(input_, res, intervals_list)   


intervals_list.clear()
intervals_set.clear()
input_ = ((1, 3), (9, 11), (2, 10))
res = (2, 4, 10)
import timeit
print(min(timeit.repeat('intervals_set.clear()\ntest(input_, res, intervals_set)', 'from __main__ import test, input_, res, intervals_set')))
print(min(timeit.repeat('intervals_list.clear()\ntest(input_, res, intervals_list)', 'from __main__ import test, input_, res, intervals_list')))
# test(input_, res, intervals_set)   
# test(input_, res, intervals_list)   

intervals_list.clear()
intervals_set.clear()
input_ = ((1, 2), (50, 57), (10, 11), (1, 11))
res = (1, 8, 9, 17)
import timeit
print(min(timeit.repeat('intervals_set.clear()\ntest(input_, res, intervals_set)', 'from __main__ import test, input_, res, intervals_set')))
print(min(timeit.repeat('intervals_list.clear()\ntest(input_, res, intervals_list)', 'from __main__ import test, input_, res, intervals_list')))
# test(input_, res, intervals_set)   
# test(input_, res, intervals_list) 
