'''
Given a two dimensional array containing only integers, implement a NextMinIterator class that has two functions: next() and hasNext(). next() returns the next minimum item from the input while hasNext() returns a boolean value indicating whether the iterator has reached the end. Each sub-array is pre-sorted in ascending order.

Example: [
[0, 2, 29],
[3, 4, 7],
[1, 5, 8, 10]]

calling next() 6 times returns -> 0, 1, 2, 3, 4, 5 calling hasNext() returns true

calling next() 10 times returns -> 0, 1, 2, 3, 4, 5, 7, 8, 9, 10 calling hasNext() returns false

t: 
    init: m+n --> O(min(m,n))
    next: lg(m+n) --> O(m,n)
    hasnext: 1
'''
from heapq import heapify, heappop, heappush
class NextMinIterator_Old:

    def __init__(self, arr):
        print("hi")
        self.arr = []
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                self.arr.append(arr[i][j])
        heapify(self.arr)
        
    def hasNext(self):
        return bool(self.arr)

    def next(self):
        return heappop(self.arr)

    
'''
init                                          sss
    colloc = [0] * len(arr) 
    for idx, row in enumerate(arr):
        heap.append((row[0], idx))  # val, row,

next
    val, row = pop() # 
    colloc[tup[1]] += 1
    val = arr[][]
    heapappend( val,  )
    return tup[0]
'''
class NextMinIterator:

    def __init__(self, arr):
        self.origarr = arr
        self.collookup = [0] * len(arr) 
        self.arr = []
        for idx, row in enumerate(arr):
            heappush(self.arr, (row[0], idx))  # val, row,
        
    def hasNext(self):
        return bool(self.arr)

    '''
    [0, 2, 29],
    [3, 4, 7],
    [1, 5, 8, 10]    
    '''
    def next(self):
        val, row = heappop(self.arr) # 
        col = self.collookup[row]
        if col + 1 < len(self.origarr[row]):
            heappush(self.arr, (self.origarr[row][col + 1], row))
            self.collookup[row] += 1
        return val
        
arr = [[0, 2, 9],[3, 4, 7],[1, 5, 8, 10]]
iter_ = NextMinIterator(arr)
count = 100
while iter_.hasNext() and count > 0:
    print(iter_.next(), end=", ")
    count -= 1
print()
    
