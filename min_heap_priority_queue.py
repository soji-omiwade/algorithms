class MinHeapPriorityQueue:
    def __init__(self, a):
        self.a = a
        self.build_max_heap()
        
    def __len__(self):
        return len(self.a)
        
    def extract_min(self):
        if len(self.a) == 0:
            raise Exception("priority queue is empty")
        val = self.a[0]
        pop_val = self.a.pop()
        if len(self.a) > 0:
            self.a[0] = pop_val
            self.heapify(0)
        return val
    
    def parent(self, i):
        return (i-1)//2

    def insert(self, size):
        a = self.a
        p = self.parent
        def float(i):
            if p(i) >= 0 and a[i] < a[p(i)]:
                a[i], a[p(i)] = a[p(i)], a[i]
                float(p(i))
        self.a.append(size)
        float(len(a)-1)
    

    def build_max_heap(self):
        for i in range(self.parent(len(self.a)-1), -1, -1):
            self.heapify(i)
        
    def heapify(self, i):
        a = self.a
        def left(i):
            return 2*i + 1
        def right(i):
            return 2*i + 2
        smallest = i
        if left(i) < len(a) and a[left(i)] < a[smallest]:
            smallest = left(i)
        if right(i) < len(a) and a[right(i)] < a[smallest]:
            smallest = right(i)
        if smallest != i:
            a[smallest], a[i] = a[i], a[smallest]
            self.heapify(smallest)


            
    