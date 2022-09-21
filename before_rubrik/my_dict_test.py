from my_dict import LinkedListDict
from random import random, randrange, shuffle

n = 10
lld = LinkedListDict(n)
for i in range(1000):
    lld.add(i)
assert lld.get_list(42) == 42 % n
assert lld.get_list(89) == 89 % n
assert lld.get_list(209) == 209 % n
assert lld.get_list(420) == 420 % n


n = 7
lld = LinkedListDict(n)
for i in range(1000):
    lld.add(i)
assert lld.get_list(42) == 42 % n
assert lld.get_list(89) == 89 % n
assert lld.get_list(209) == 209 % n
assert lld.get_list(420) == 420 % n
