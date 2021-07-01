class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method
    
    
class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
            
mc = Mapping([2,3,4])
for x in mc.items_list:
    print(x, end=", ")
print()
print(Mapping.update)
Mapping._Mapping__update(mc, [8,9,9])
for x in mc.items_list:
    print(x, end=", ")
print()

msc = MappingSubclass([2,3,4])
msc.update([5],[7])
for x in msc.items_list:
    print(x, end=", ")
print()
