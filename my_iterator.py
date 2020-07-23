class MyIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.it = iter(self.iterable)
    
    def __next__(self):
        next(self.it)
        return next(self.it)

class MyHopOverList:
    def __init__(self, n):
        self._iterable = range(n)

    def __iter__(self):
        return MyIterator(self._iterable)



# print([x**2 for x in MyHopOverIterable(10)])
assert [x**2 for x in MyHopOverList(10)] == [1, 9, 25, 49, 81]