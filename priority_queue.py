'''
API allow you to add prioritized items to a service
add p-item
summon item so I can delete it
summon item, so I can update priority

pq = PriorityQueue()
pq.additem(item, priority)
pq.delitem(item) -> item
pq.update_item(item)
pq.pop_item() -> item
'''


from collections import Counter
from heapq import heappush, heappop

class PriorityQueue:
    def __init__(self):
        self.arr = []
        self.entry_finder = {}
        
    REMOVED = "<REMOVED>"
    '''
    p-items can always be compared
    p-item: (priority, count, item)
    '''
    def additem(self, item, priority):
        pitem = [priority, next(counter), item]
        self.entry_finder[item] = pitem
        heappush(self.arr,  pitem)
        
    def delitem(self, item):
        pitem = self.entry_finder.pop()
        pitem[-1] = REMOVED
        return pitem
        
    def update_item(self, item, priority):
        self.delitem(item)
        self.additem(item, priority)
        
    def popitem(self, item):
        while self.arr:
            pitem = heappop()
            if pitem[-1] is not REMOVED:
                del self.entry_finder[pitem[-1]]
                return pitem
                