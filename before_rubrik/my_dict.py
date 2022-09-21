class LinkedListDict:
    class LinkedList:
        class Node:
            def __init__(self, val, next=None, prev=None):
                self.next = next
                self.prev = prev
                self.val = val
                
        def __init__(self):
            self.head = LinkedListDict.LinkedList.Node(None)
            self.tail = LinkedListDict.LinkedList.Node(None)
            self.head.next, self.tail.prev = self.tail, self.head
            
        def insert(self, val):
            v = LinkedListDict.LinkedList.Node(val)
            v.next = self.head.next
            self.head.next.prev = v
            self.head.next = v
            v.prev = self.head
        
    def __init__(self, n: int):
        """n is the number of linked lists. 
        
        n is not the capacity, cap is infinite for now
        """
        self.table = []
        for i in range(n):
            self.table.append(LinkedListDict.LinkedList())
        
    def add(self, val: int):
        self.table[self.h(val)].insert(val)
        
    def h(self, value):
        return value % len(self.table)
        
    def get_list(self, value):
        for i in range(len(self.table)):
            hlist = self.table[i]
            v = hlist.head
            while v is not hlist.tail:
                if v.val == value:
                    return i
                v = v.next
        return -1
                