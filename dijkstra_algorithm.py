class PriorityQueue:
    def is_empty(self):
        return self.n == 0
    def decrease_key(self, i, key):
        self.heap.a[i] = key
        self.heap.heapify(i)
    def extract_min(self):
        key=self.heap.a[0]
        a[0]=a[n-1]
        self.heap.n-=1
        self.heap.heapify(0)
        return key
    
    class MinHeap:
