import math
class GraphPriorityQueue:
    def __init__(self, n, src):
        self.heap = self.MinHeap(n, src)
    
    def is_empty(self):
        return self.heap.size == 0
        
    def decrease_key(self, v_key, key):
        i = self.heap.b[v_key]
        if key > self.heap.a[i]:
            raise ValueError("new key is greater than current key")
        self.heap.a[i] = key
        self.heap.reverse_heapify(i)
        
    def extract_min(self):
        if self.heap.size < 1: 
            raise Exception(f"heap underflow at size {self.heap.size}")
        min_key = self.heap.b[0]
        self.heap.a[0] = self.heap.a[self.heap.size-1]
        self.heap.b[0] = self.heap.b[self.heap.size-1]
        self.heap.size -= 1
        self.heap.heapify(0)
        return min_key
    
    class MinHeap:
        def __init__(self, n, src):
            self.a = [math.inf for _ in range(n)]
            self.a[src] = 0
            self.b = [i for i in range(n)]
            self.size = n
            for i in range(math.floor(self.size/2)-1, -1, -1):
                self.heapify(i)
                
        def parent(self, i):
            return math.floor((i-1)/2)
            
        def left(self, i):
            return 2*i + 1
            
        def right(self, i):
            return 2*(i+1)
                 
        def reverse_heapify(self, i):
            while i > 0 and self.a[self.parent(i)] > self.a[i]:
                self.a[i], self.a[self.parent(i)] = self.a[self.parent(i)], self.a[i]
                self.b[i], self.b[self.parent(i)] = self.b[self.parent(i)], self.b[i] 
                i = self.parent(i)
       
        def heapify(self, i): 
            l = self.left(i)
            r = self.right(i)
            smallest = i
            if l < self.size and self.a[l] < self.a[i]:
                smallest = l
            if r < self.size and self.a[r]< self.a[smallest]:
                smallest = r
            if smallest != i:
                self.a[i], self.a[smallest]= self.a[smallest], self.a[i]
                self.b[i], self.b[smallest] = self.b[smallest], self.b[i]
                self.heapify(smallest)