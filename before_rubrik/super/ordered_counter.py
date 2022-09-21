from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    "counter that remembers the order elements are first seen"
    # def __repr__(self):
        # return "%s(%r)" % (__class__.__name__, OrderedDict(self))
        
    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)
    pass    
oc = OrderedCounter("abracadabra")
print(oc)
# print(list(oc.elements()))