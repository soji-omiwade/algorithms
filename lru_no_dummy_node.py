class DLL:
    class Node:
        def __init__(self, val):
            self.val = val
            self.prev = self.next = None
            
    def __init__(self):
        self.head = None
        self.tail = None
        
    def remove(self, node: "DLL.Node") -> "DLL.Node":
        if (self.head is self.tail is None) or not node:
            raise Exception("impossible: lookup said node is here!")
            
        if node is self.head:
            self.head = node.next
            if not self.head:
                self.tail = None
            return
        if node is self.tail:
            self.tail = node.prev
            self.tail.next = None
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def add(self, node):
        if self.head is self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
               
        
node1 = DLL.Node(1)
node5 = DLL.Node(5)
node2 = DLL.Node(2)

dlis = DLL()
dlis.add(node5)
dlis.add(node1)
dlis.add(node2)

print(dlis.head.val) #5
print(dlis.head.next.val) #1
print(dlis.head.next.next.val) #2
print(dlis.head.next.next.next)
print()

dlis.remove(node1)
print(dlis.head.val) #5
print(dlis.head.next.val) #2
print(dlis.head.next.next) #null
print()

dlis.remove(node2)
print(dlis.head.val) #5
print(dlis.head.next) # null
print()

dlis.remove(node5)
print(dlis.head) #null
print()

node1 = DLL.Node(1)
node5 = DLL.Node(5)
node2 = DLL.Node(2)

dlis = DLL()
dlis.add(node5)
dlis.add(node1)
dlis.add(node2)

print(dlis.head.val) #5
print(dlis.head.next.val) #1
print(dlis.head.next.next.val) #2
print(dlis.head.next.next.next) #null
