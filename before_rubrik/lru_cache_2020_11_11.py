class LRUCache:
    class Node:
        def __init__(self, key: int = None, value: int = None):
            self.key = key
            self.value = value
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next, self.tail.prev = self.tail, self.head
        self.lookup = dict()

    def _append(self, node: Node) -> None:
        tail_prev = self.tail.prev
        node.prev, node.next = tail_prev, self.tail
        tail_prev.next = self.tail.prev = node
        
    def _popleft(self) -> Node:
        head_next = self.head.next
        self._extract(head_next)
        return head_next
    
    def _extract(self, node: Node) -> None:
        node.prev.next, node.next.prev = node.next, node.prev
        
    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        res = self.lookup[key]
        self._extract(res)
        self._append(res)
        return res.value
        
    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            self.lookup[key].value = value
        else:
            node = self.Node(key, value)
            self._append(node)
            self.lookup[key] = node
            if len(self.lookup) > self.capacity:
                del self.lookup[self._popleft().key]

# Your LRUCache object will be instantiated and called as such:
cmds = ["LRUCache","put","put","get","put","get","put","get","get","get"]
paramlists = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
actual = [None, None, None, 1, None, -1, None, -1, 3, 4]
res = []
for cmd, paramlist in zip(cmds,paramlists):
    if cmd == "LRUCache": 
        cache = LRUCache(paramlist[0])
        res.append(None)
    elif cmd == "put":
        cache.put(*paramlist)
        res.append(None)
    elif cmd == "get":
        res.append(cache.get(*paramlist))

print(res)
assert res == actual