class ListPriorityQueue:
    pass
class MinHeapPriorityQueue:
    def __init__(self, a):
        self.a = list(a)
        self.build_min_heap(self.a)

    def heapify(self, i):
        def left(i):
            return 2*i + 1
        def right(i):
            return 2*i + 2

        smallest = i
        if left(i) < len(self.a) and self.a[left(i)] < self.a[i]:
            smallest = left(i)
        if right(i) < len(self.a) and self.a[right(i)] < self.a[smallest]:
            smallest = right(i)
        
        if smallest != i:
            self.a[i],self.a[smallest] = self.a[smallest],self.a[i]
            self.heapify(smallest)
        
    def build_min_heap(self, a):
        for i in range(len(self.a)//2-1,-1,-1):
            self.heapify(i)
    
    def extract_min(self):
        val = self.a[0]
        new_first = self.a.pop()
        if len(self.a) > 0:
            self.a[0] = new_first
            self.heapify(0)
        return val
        
    def insert(self, val):
        def parent(i):
            return (i-1)//2
        def float_key(k):
            if k == 0:
                return
                
            if self.a[k] < self.a[parent(k)]:
                self.a[k], self.a[parent(k)] = self.a[parent(k)],self.a[k]
                float_key(parent(k))            
        self.a.append(val)
        float_key(len(self.a)-1)
        
    def __len__(self):
        return len(self.a)
        
if __name__ == "__main__":
    arr = [1,1,1, 1,1,1, 1,1,1]
    from random import shuffle
    shuffle(arr)
    pq = \
    MinHeapPriorityQueue(arr)
    # ListPriorityQueue(arr)
    cost = 0
    while len(pq) > 1:
        a = pq.extract_min()
        b = pq.extract_min()
        pq.insert(a+b)
        cost += a+b
    print(cost)