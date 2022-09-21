'''
x1---3 2 
3 2

delete(val)
    if val not in loc:
        return False
    valloc = loc[val]
    nums[valloc] = nums[-1]
    loc[nums[-1]] = valloc
    del loc[val]
    nums.pop()
    return True

2 1 5 42
insert(val)
    if val in loc:
        return True
    nums.append(val)
    loc[val] = len(nums) - 1
    
random()
    nums[randrange(len(nums))]
    
d[1] = count ++ 


[1 x 3]
del d[1]

1 2 3 4 5 6 
'''
#from random import randrange
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.loc = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.loc:
            return False
        self.nums.append(val)
        self.loc[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.loc:
            return False
        valloc = self.loc[val]
        self.nums[valloc] = self.nums[-1]
        self.loc[self.nums[-1]] = valloc
        del self.loc[val]
        self.nums.pop()
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.nums[randrange(len(self.nums))]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()