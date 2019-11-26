class TwoStackQueue:

    def __init__(self, foo=None):
        if foo is None:
            foo = []
        self.s1 = foo
        self.s2 = []
        
    def enqueue(self,x):
        if not self.s1:
            self.s1 = self.s2[-1::-1]
            self.s2 = []
        self.s1.append(x)
        
    def dequeue(self):
        if not self.s2: 
            self.s2 = self.s1[-1::-1]
            self.s1 = []
        return self.s2.pop() if self.s2 else None
        
    def __repr__(self):
        if self.s1: return str(self.s1)
        if self.s2: return str(self.s2[-1::-1])
        
tsq = TwoStackQueue([9, 98, 42, 1, 3])
print(tsq)