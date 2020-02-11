class ListPriorityQueue:
    def __init__(self, a):
        self.a = list(a)
        self.extract_starts = False
        
    def extract_min(self):
        def arr_to_list(a):
            if a is None:
                raise Exception ("Empty List")
            
        class Node:
            def __init__(self, key, head):
                self.key = key
                self.next = head
                
            """list to array conversion"""
            head = None
            for i in range(len(a),-1,-1):
                head = Node(a[i], head)


            return head
            
        if not self.extract_starts:
            self.extract_starts = True
            self.h = arr_to_list()
        
        val = self.h
        self.h = self.h.next
        return val
    def insert(self):
        
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
    # [1,2,3,4,5,6]
    arr = \
    [1,1,1, 1,1,1, 1,1,1]
    from random import shuffle
    shuffle(arr)
    pq = MinHeapPriorityQueue(arr) 
    # pq = ListPriorityQueue(arr)
    cost = 0
    while len(pq) > 1:
        a = pq.extract_min()
        b = pq.extract_min()
        pq.insert(a+b)
        cost += a+b
    print(cost)