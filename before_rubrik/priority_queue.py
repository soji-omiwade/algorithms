'''
API allow you to add prioritized items to a service
add item
delete item
get min-priority item
'''

from itertools import count
from heapq import heappush, heappop

class PriorityQueue:
    def __init__(self):
        self.arr = []
        self.entry_finder = {}
        
    REMOVED = "<REMOVED>"
    counter = count()
    '''
    p-items can always be compared
    p-item: (priority, count, item)
    '''
    def additem(self, item, priority):
        if item in self.entry_finder:
            self.delitem(item)
        pitem = [priority, next(self.counter), item]
        self.entry_finder[item] = pitem
        heappush(self.arr,  pitem)
        
    def delitem(self, item):
        pitem = self.entry_finder.pop(item)
        pitem[-1] = self.REMOVED
               
    def popitem(self):
        while self.arr:
            pitem = heappop(self.arr)
            if pitem[-1] is not self.REMOVED:
                del self.entry_finder[pitem[-1]]
                return pitem
        raise KeyError("pop from an empty queue")        