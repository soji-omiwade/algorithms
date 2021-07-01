class LinkedList:
    class Node: 
        def __init__(self, key=None):
            self.key = key
            self.prev = self.next = self.value = None
        
        
    def __init__(self):
        self.head = LinkedList.Node()
        self.tail = LinkedList.Node()
        self.head.next, self.tail.prev = self.tail, self.head
        
    def add_to_front(self, node) -> None:
        node.prev, node.next = self.head, self.head.next
        self.head.next = node.next.prev = node

    def move_to_front(self, node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        self.add_to_front(node)       

    def remove_tail(self) -> Node:
        if self.head.next is self.tail:
            return None
        res = self.tail.prev
        res.prev.next = self.tail
        self.tail.prev = res.prev
        return res
    
    
class LRU: 
    def __init__(self, MAX_SIZE):
        self.lookup = {}
        self.llist = LinkedList()
        self.MAX_SIZE = MAX_SIZE
        for i in range(MAX_SIZE):
            self.memset(i, 10 * i)
            
    def see_cache(self) -> None:
        curr = self.llist.head.next
        while curr is not self.llist.tail:
            print(f"{(curr.key, curr.value)}", end=", ")
            curr = curr.next
        print()
        
    def memset(self, key, value):
        '''
        node = lookup[key]
        move node to front
        node.value = value
        '''
        if key in self.lookup:
            node = self.lookup[key]
            self.llist.move_to_front(node)
        else:
            if len(self.lookup) == self.MAX_SIZE:
                self.lookup.pop(self.llist.remove_tail().key)
            node = LinkedList.Node(key)
            self.lookup[key] = node
            self.llist.add_to_front(node)
        node.value = value
        print(f"{(key, value)} inserted")
        
    def memget(self, key):
        '''
        try: 
            return self.lookup[key]
        except KeyError:
            return None
        '''
        if key in self.lookup:
            self.llist.move_to_front(self.lookup[key])
            return self.lookup[key].value
        

cache = LRU(5)
cache.see_cache() # 4 3 2 1 0
print(f"0? = {cache.memget(0)}")
cache.see_cache() # 0 4 3 2 1
cache.memset(3, 300)
cache.see_cache() # 3 0 4 2 1
print(f"4? = {cache.memget(4)}")
cache.see_cache() # 4 3 0 2 1
