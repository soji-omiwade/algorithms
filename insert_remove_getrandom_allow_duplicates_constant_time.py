'''
input 1 1 2 r1
output -> 1 2

vals: array
loc: dictionary of arrays and array is locs for the key

[1, 1, 1]
insert:
    if it in dictionary we are going to return False.
    But still need to add it as follows:
        add it to end of vals
        update dictionary with that loc: 
            add to back of locations[val] the location == len(vals) - 1
        
getrandom
    random one of them
    
[3] -->[4]   
[2]->[6, 9] ---> [6, 4]
vals[...locations7...2]
delete (3)
    if not in dict return false
    newloc = pop from 3's vals.......7
    get last val in vals equal (2)
    put it in elem's loc we want deleted  vals[newloc] = vals[-1]
    pop from vals
    update dictionary for added element locations[newloc][-1] = newloc
    delete dict entry for val 
        if locations[val] is empty
            del loc [val]
'''
class RandomizedCollection:
    from collections import defaultdict
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = []
        self.locations = defaultdict(set) # locations[1] = set
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        already_exists = True
        if val in self.locations:
            already_exists = False
        self.vals.append(val)
        self.locations[val].add(len(self.vals) - 1)
        return already_exists

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.locations:
            return False
        lastval = self.vals[-1]             # 1
        valloc = self.locations[val].pop()  # 0
        self.vals[valloc] = lastval         # [1]
        self.locations[lastval].add(valloc) # {0}
        self.locations[lastval].remove(len(self.vals) - 1)      # {0:empty}
        self.vals.pop()                                         # []
        if not self.locations[val]:
            del self.locations[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        from random import choice
        return choice(self.vals)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()