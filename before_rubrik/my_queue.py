import sys
class my_queue:
    class _Node:
        def __init__(self, val):
            self.val = val
            self.next = None
            
    def __init__(self):
        self._head = None
        self._tail = None

    def append(self, el):
        v = self._Node(el)
        if not self._head:
            self._head = self._tail = v
        else:
            self._tail.next = v
            self._tail = v

    def popleft(self):
        try:
            res = self._head.val
            self._head=self._head.next
        except:
            print("list may be empty",file=sys.stderr)
        else:
            return res
        
    def show(self):
        v = self._head
        while v:
            print(f"{v.val}, ",end="")
            v=v.next
        print()

q=my_queue()
q.append("42")
q.append(42)
q.show()
q.popleft()
q.show()
q.popleft()
q.show()
q.popleft()
q.append(4)
q.append("me")
q.show()
