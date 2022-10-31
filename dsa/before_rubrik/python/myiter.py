from datetime import datetime



class MyIter:
    def __init__(self, count):
        self.idx = 0
        self.count = count
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.idx == self.count:
            raise StopIteration
        res = (self.idx, datetime.now().strftime("%H:%M:%S"))
        self.idx += 1
        return res
        
for x,t in MyIter(100000):
    if (x % 10000) == 0:
        print(f"{(x, t)}", end="\n")
print()