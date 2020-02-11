class ListPriorityQueue:
    class Node:
        def __init__(self, size):
            self.size = size
            self.next = self.prev = None

    def __len__(self):
        return self.count
        
    def __init__(self, a):
        a.sort()
        self.head = None
        self.count = len(a)
        for i in range(len(a)-1,-1,-1):
            v = ListPriorityQueue.Node(a[i])
            if self.head is None:
                self.head = v
                continue
            v.next, self.head.prev = self.head, v
            self.head = v
            
            
    def insert(self, size):
        if self.head is None:
            self.head = ListPriorityQueue.Node(size)
            return

        w = ListPriorityQueue.Node(size)
        v = self.head
        while v:
            if size < v.size:
                if v.prev is None: #i.e., v is the self.head
                    self.head = w
                else:
                    u = v.prev
                    u.next, w.prev = w, u
                w.next, v.prev = v, w
                break
            if v and not v.next:
                last = v
            v=v.next
        if w.next is None: #it hasn't been set bcos w.size > max-size
            last.next, w.prev = w, last
        self.count += 1    
            
    def extract_min(self):
        if self.head is None:
            raise Exception("priority queue is empty")
        val = self.head.size
        self.head = self.head.next
        self.count -= 1
        return val
        
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
        """O(n)?"""
        for i in range(self.parent(len(self.a)-1),-1,-1):
            self.heapify(i)
    
    def extract_min(self):
        """O(lg n)"""
        val = self.a[0]
        new_first = self.a.pop()
        if len(self.a) > 0:
            self.a[0] = new_first
            self.heapify(0)
        return val

    @staticmethod
    def parent(i):
        return (i-1)//2
        
    def insert(self, val):
        """O(lg n)"""
        def float_key(k):
            if k == 0:
                return
                
            if self.a[k] < self.a[self.parent(k)]:
                self.a[k], self.a[self.parent(k)] = (
                    self.a[self.parent(k)], self.a[k])
                float_key(self.parent(k))            
        self.a.append(val)
        float_key(len(self.a)-1)
        
    def __len__(self):
        return len(self.a)
        
if __name__ == "__main__":
    import sys
    # arr =  [1,2,3,4,5,6]
    arr = [1,1,1, 1,1,1, 1,1,1]
    from random import shuffle
    shuffle(arr)
    if sys.argv[1] == "0":
        pq = MinHeapPriorityQueue(arr) 
    else: 
        pq = ListPriorityQueue(arr)
    cost = 0
    while len(pq) > 1:
        a = pq.extract_min()
        b = pq.extract_min()
        pq.insert(a+b)
        cost += a+b
    print(cost)