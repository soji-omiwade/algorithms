"""
A clean linked-list implementation in under an hour with unittest cases!
"""

class MyList:  
    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next
    def __init__(self):
        self.head = None
    def insert(self, val: int):
        if self.head: 
           self.head = MyList.Node(val, self.head)
        else: 
            self.head = MyList.Node(val)
    def _search(self, val: int):
        v = self.head
        u = self.head
        while v:
            if v.val == val:
                return u,v
            u,v = v,v.next
            
        return None, None
    def delete(self, val: int):
        u,v = self._search(val)
        if v:
            if u: 
                u.next = v.next
            else:
                assert(v == self.head)
                self.head = self.head.next
        return v
    def _node_search(self, v):
        u = self.head
        while u:
            if u is v:
                return u
            u = u.next
        return None
    def update(self, w: Node, new_val: int):
        v = self._node_search(w)
        if v: 
            v.val = new_val
            return v
        return None
    def to_list(self):
        v = self.head
        res = []
        while v:
            res.append(v.val)
            v = v.next
        return res
