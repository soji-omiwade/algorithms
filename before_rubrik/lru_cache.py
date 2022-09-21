class LRUCache:
    class ListNode:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = self.prev = None
            
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = LRUCache.ListNode(None, None)
        self.tail = LRUCache.ListNode(None, None)
        self.head.next, self.tail.prev = self.tail, self.head
        self.count = 2
        self.d = {}
        
    def print_cache(self):
        v = self.head.next
        while v.key != None:
            print(v.key, end=", ")
            v = v.next
        print()
        
    def get(self, key: int) -> int:
        v = self.tail
        if key in self.d:
            v = self.d[key]
        if v is not self.tail:
            v.prev.next = v.next
            v.next.prev = v.prev
            v.next = self.head.next
            self.head.next.prev = v
            self.head.next = v
            v.prev = self.head
            return v.value
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if self.get(key) != -1:
            self.head.next.value = value
        else:
            v = LRUCache.ListNode(key,value)
            self.d[key] = v
            v.next = self.head.next
            self.head.next.prev = v
            self.head.next = v
            v.prev = self.head
            self.count += 1
            if self.count == self.capacity + 3:
                del self.d[self.tail.prev.key]
                self.tail.prev = self.tail.prev.prev
                self.tail.prev.next = self.tail
                self.count -= 1            

# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
assert obj.get(1) == -1
obj.put(1,10)
obj.put(2,20)
assert obj.get(2) == 20
assert obj.get(1) == 10
obj.put(3,30)
assert obj.get(1) == 10
assert obj.get(2) == -1
obj.put(4,40)
assert obj.get(1) == 10
assert obj.get(3) == -1
assert obj.get(4) == 40