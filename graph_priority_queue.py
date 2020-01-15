class GraphPriorityQueue:
    def __init__(self, g:dict, src:int):
        a = [None]
        for i in range(1,1+len(g)):
            a.append((math.inf, g[i-1]))
        a[src+1] = 0
        self.heap = self.MinHeap(a)
        
    def is_empty(self):
        return self.heap.size == 0
        
    def decrease_key(self, i, key):
        i += 1
        if key > self.heap.a[i]:
            raise ValueError("new key is greater than current key")
        self.heap.a[i] = key
        self.heap.heapify(i)
        
    def extract_min(self):
        if self.heap.size < 1: 
            raise Exception(f"heap underflow at size {self.heap.size}")
        min_key=self.heap.a[1]
        self.heap.a[1]=self.heap.a[self.heap.size]
        self.heap.size -= 1
        self.heap.heapify(1)
        return min_key[1]
    
    class MinHeap:
        def __init__(self, a):
            self.a = a
            self.size = len(a)-1
            for i in range(math.floor(self.size/2), 0, -1):
                self.heapify(i)
                
        def left(self, i):
            return 2*i
            
        def right(self, i):
            return 2*i+1
            
        def pi(self, i):
            return math.floor(i/2)
            
        def heapify(self, i): 
            l = self.left(i)
            r = self.right(i)
            smallest = i
            if l <= self.size and self.a[l] < self.a[i]:
                smallest = l
            if r <= self.size and self.a[r] < self.a[smallest]:
                smallest = r
            if smallest != i:
                self.a[i],self.a[smallest] = self.a[smallest],self.a[i]
                self.heapify(smallest)
